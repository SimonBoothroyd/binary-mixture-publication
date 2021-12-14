import os
from typing import List

import pandas
from nonbonded.library.models.authors import Author
from nonbonded.library.models.datasets import DataSet
from openff.evaluator.utils.checkmol import ChemicalEnvironment
from openff.evaluator.datasets.curation.components import (
    conversion,
    filtering,
    selection,
    thermoml,
)
from openff.evaluator.datasets.curation.components.selection import State, TargetState
from openff.evaluator.datasets.curation.workflow import (
    CurationWorkflow,
    CurationWorkflowSchema,
)
from source_h_vap_data import source_enthalpy_of_vaporization


AUTHORS = [
    Author(
        name="Simon Boothroyd",
        email="simon.boothroyd@colorado.edu",
        institute="University of Colorado Boulder",
    ),
    Author(
        name="Owen Madin",
        email="owen.madin@colorado.edu",
        institute="University of Colorado Boulder",
    ),
]

N_PROCESSES = 4

UPLOAD = False


def prepare_initial_data() -> pandas.DataFrame:
    """This function pulls all of the available (and parsable) data from
    the ThermoML archive and from the hand sourced enthalpy of vaporization
    data points, and applies a set of common filters.

    This data is expected to be used as the starting point for the data set
    curations.

    Returns
    -------
        The extracted data.
    """

    # Import the sourced enthalpy of vaporization data.
    sourced_h_vap_data = source_enthalpy_of_vaporization()

    # Pull down all of the usable data from ThermoML.
    initial_data = CurationWorkflow.apply(
        data_set=sourced_h_vap_data,
        schema=CurationWorkflowSchema(
            component_schemas=[
                # Pull down the data from ThermoML.
                thermoml.ImportThermoMLDataSchema(),
                # Retain only data points measured for pure and binary systems.
                filtering.FilterByNComponentsSchema(n_components=[1, 2]),
                # Remove duplicate data
                filtering.FilterDuplicatesSchema(),
                # Filter out only the properties of interest.
                filtering.FilterByPropertyTypesSchema(
                    property_types=[
                        "Density",
                        "EnthalpyOfVaporization",
                        "EnthalpyOfMixing",
                        "ExcessMolarVolume",
                    ],
                    n_components={
                        "Density": [1, 2],
                        "EnthalpyOfVaporization": [1, 2],
                        "EnthalpyOfMixing": [2],
                        "ExcessMolarVolume": [2],
                    },
                ),
                # Filter by temperature and pressure,
                filtering.FilterByTemperatureSchema(
                    minimum_temperature=288.15, maximum_temperature=323.15
                ),
                filtering.FilterByPressureSchema(
                    minimum_pressure=0.95 * 101.325, maximum_pressure=1.05 * 101.325
                ),
                # Remove any elements which aren't of interest for this study.
                filtering.FilterByElementsSchema(allowed_elements=["C", "O", "H"]),
                # Filter out molecules with undefined stereochemistry
                filtering.FilterByStereochemistrySchema(),
                # Filter out charged or ionic liquids,
                filtering.FilterByChargedSchema(),
                filtering.FilterByIonicLiquidSchema(),
                # Filter out any molecules which do not contain the chemical
                # functionality of interest.
                filtering.FilterByEnvironmentsSchema(
                    environments=[
                        ChemicalEnvironment.Hydroxy,
                        ChemicalEnvironment.CarboxylicAcidEster,
                        ChemicalEnvironment.CarboxylicAcid,
                        ChemicalEnvironment.Ether,
                        ChemicalEnvironment.Ketone,
                        ChemicalEnvironment.Alkane,
                    ]
                ),
            ]
        ),
        n_processes=N_PROCESSES,
    )

    return initial_data


def curate_pure_training_sets(initial_data: pandas.DataFrame) -> List[DataSet]:
    """Curate the pure training set.

    Parameters
    ----------
    initial_data
        A data frame containing all of the available data to
        select data points from.
    """

    schema = CurationWorkflowSchema(
        component_schemas=[
            # Retain only enthalpy of vaporization and density data points
            # which were measured for the same pure systems.
            filtering.FilterByPropertyTypesSchema(
                property_types=["Density", "EnthalpyOfVaporization"],
                n_components={"Density": [1], "EnthalpyOfVaporization": [1]},
                strict=True,
            ),
            # Filter out all but the hand selected systems.
            filtering.FilterBySmilesSchema(
                smiles_to_include=[
                    # Ethers
                    "C1COCCO1",
                    "C1CCOCC1",
                    "COC(C)(C)C",
                    "CC(C)OC(C)C",
                    "CCCCOCCCC",
                    # Ketones
                    "O=C1CCCC1",
                    "CCCC(C)=O",
                    "O=C1CCCCC1",
                    "O=C1CCCCCC1",
                    # Alcohols
                    "CO",
                    "CCO",
                    "CCCO",
                    "CCCCO",
                    "CC(C)(C)O",
                    "CC(C)O",
                    "CC(C)CO",
                    # Esters
                    "CC(=O)O",
                    "COC=O",
                    "CCOC(C)=O",
                    "CCOC(=O)CC(=O)OCC",
                    "CCCCOC(C)=O",
                    "CCCOC(C)=O",
                    # Alkanes
                    "C1CCCCC1",
                    "CCCCCC",
                    "CC1CCCCC1",
                    "CCCCCCC",
                    "CC(C)CC(C)(C)C",
                    "CCCCCCCCCC",
                ]
            ),
            # Select data points close to ambient conditions
            selection.SelectDataPointsSchema(
                target_states=[
                    TargetState(
                        property_types=[("Density", 1), ("EnthalpyOfVaporization", 1)],
                        states=[
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(1.0,),
                            )
                        ],
                    )
                ]
            ),
        ],
    )

    # Apply the curation schema to yield the training set.
    training_data_frame = CurationWorkflow.apply(initial_data, schema, N_PROCESSES)

    rho_training_data = training_data_frame[
        training_data_frame["Density Value (g / ml)"].notna()
    ]
    h_vap_training_data = training_data_frame[
        training_data_frame["EnthalpyOfVaporization Value (kJ / mol)"].notna()
    ]

    training_sets = [
        DataSet.from_pandas(
            data_frame=rho_training_data,
            identifier="bmfs-exp-train-rho",
            description="A data set composed of density measurements made for "
            "pure systems of alcohols, ethers, ketones, alkanes, and esters (+ acids). "
            "The measurements were all made at close to ambient conditions."
            "\n\n"
            "The components that each of the measurements were made for are the same "
            "as those which appear in the binary mixtures found in the "
            "`bmfs-exp-train-h-mix`, `bmfs-exp-train-rho-x` data sets."
            "\n\n"
            "This data set was originally curated for the `expanded` study as part of "
            "the `binary-mixture` project",
            authors=AUTHORS,
        ),
        DataSet.from_pandas(
            data_frame=h_vap_training_data,
            identifier="bmfs-exp-train-h-vap",
            description="A data set composed of enthalpy of vaporization "
            "measurements made for pure systems of alcohols, ethers, ketones, alkanes, "
            "and esters (+ acids). The measurements were all made at close to ambient "
            "conditions."
            "\n\n"
            "The components that each of the measurements were made for are the same "
            "as those which appear in the binary mixtures found in the "
            "`bmfs-exp-train-h-mix`, `bmfs-exp-train-rho-x` data sets."
            "\n\n"
            "This data set was originally curated for the `expanded` study as part of "
            "the `binary-mixture` project",
            authors=AUTHORS,
        )
    ]

    return training_sets


def curate_mixture_training_sets(initial_data: pandas.DataFrame) -> List[DataSet]:
    """Curate the mixture training set.

    Parameters
    ----------
    initial_data
        A data frame containing all of the available data to
        select data points from.
    """

    # Apply the curation schema to yield the training set.
    schema = CurationWorkflowSchema(
        component_schemas=[
            # Attempt to inter-convert binary density and
            # excess molar volume data where possible.
            conversion.ConvertExcessDensityDataSchema(),
            # Remove any duplicate data.
            filtering.FilterDuplicatesSchema(),
            # Retain only enthalpy of mixing, and density data points which were
            # measured for the same binary systems.
            filtering.FilterByNComponentsSchema(n_components=[2]),
            filtering.FilterByPropertyTypesSchema(
                property_types=["Density", "EnthalpyOfMixing"],
                strict=True,
            ),
            # Filter out all but the hand selected systems.
            filtering.FilterBySubstancesSchema(
                substances_to_include=[
                    # Ether - Alkane
                    ("CCCCOCCCC", "CC(C)CC(C)(C)C"),
                    ("C1CCOCC1", "CCCCCCC"),
                    ("COC(C)(C)C", "CCCCCCCCCC"),
                    ("CC(C)OC(C)C", "CC(C)CC(C)(C)C"),
                    ("CC(C)OC(C)C", "CCCCCCC"),
                    ("C1CCOCC1", "CCCCCC"),
                    ("C1CCOCC1", "C1CCCCC1"),
                    # Alcohol - Alkane
                    ("CCCO", "C1CCCCC1"),
                    ("CCCO", "CC(C)CC(C)(C)C"),
                    ("CCCO", "CC1CCCCC1"),
                    ("CCCCO", "CC(C)CC(C)(C)C"),
                    ("CCCCO", "CCCCCC"),
                    ("CCCCO", "CC1CCCCC1"),
                    ("CCCCO", "CCCCCCC"),
                    ("CCO", "CC(C)CC(C)(C)C"),
                    ("CCO", "CCCCCCC"),
                    # Ether - Ketone
                    ("C1CCOCC1", "O=C1CCCC1"),
                    ("C1CCOCC1", "O=C1CCCCC1"),
                    ("C1CCOCC1", "CCCC(C)=O"),
                    ("C1COCCO1", "O=C1CCCC1"),
                    ("C1COCCO1", "O=C1CCCCC1"),
                    ("C1COCCO1", "CCCC(C)=O"),
                    ("C1COCCO1", "O=C1CCCCCC1"),
                    # Alcohol - Ester / Acid
                    ("CO", "COC=O"),
                    ("CO", "CCOC(=O)CC(=O)OCC"),
                    ("CCO", "CC(=O)O"),
                    ("CCO", "CCOC(C)=O"),
                    ("CCO", "CCOC(=O)CC(=O)OCC"),
                    ("CCCCO", "CCOC(=O)CC(=O)OCC"),
                    ("CC(C)O", "CCOC(=O)CC(=O)OCC"),
                    ("CC(C)CO", "CCOC(=O)CC(=O)OCC"),
                    ("CC(C)(C)O", "COC=O"),
                    ("CC(C)(C)O", "CCCCOC(C)=O"),
                ]
            ),
            # Filter to a narrower mole fraction range. This should help the
            # state point selection algorithm choose data points closer to the
            # targets.
            filtering.FilterByMoleFractionSchema(
                mole_fraction_ranges={2: [[(0.1, 0.9)]]}
            ),
            # Select data points close to ambient conditions
            selection.SelectDataPointsSchema(
                target_states=[
                    TargetState(
                        property_types=[("Density", 2), ("EnthalpyOfMixing", 2)],
                        states=[
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(0.25, 0.75),
                            ),
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(0.5, 0.5),
                            ),
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(0.75, 0.25),
                            ),
                        ],
                    )
                ]
            ),
        ]
    )
    training_data_frame = CurationWorkflow.apply(initial_data, schema, N_PROCESSES)

    rho_x_training_data = training_data_frame[
        training_data_frame["Density Value (g / ml)"].notna()
    ]
    h_mix_training_data = training_data_frame[
        training_data_frame["EnthalpyOfMixing Value (kJ / mol)"].notna()
    ]

    training_sets = [
        DataSet.from_pandas(
            data_frame=h_mix_training_data,
            identifier="bmfs-exp-train-h-mix",
            description="A data set composed of enthalpy of mixing measurements "
            "made for binary mixtures of ethers + alkanes, ethers + ketones, "
            "alcohols + alkanes, and alcohols + esters (+ acids)."
            "\n\n"
            "The measurements were all made at close to ambient conditions, and in "
            "almost all cases for three different compositions: 25%, 50% and 75%."
            "\n\n"
            "All of the systems present in this data set have corresponding density "
            "measurements in the `bmfs-exp-train-rho-x` data set. Furthermore, the "
            "densities and enthalpies of vaporization for each of the individual "
            "components in all of the binary mixtures can be found in the "
            "`bmfs-exp-train-rho` and `bmfs-exp-train-h-vap` data sets respectively."
            "\n\n"
            "This data set was originally curated for the `expanded` study as part of "
            "the `binary-mixture` project",
            authors=AUTHORS,
        ),
        DataSet.from_pandas(
            data_frame=rho_x_training_data,
            identifier="bmfs-exp-train-rho-x",
            description="A data set composed of density measurements made for "
            "binary mixtures of ethers + alkanes, ethers + ketones, "
            "alcohols + alkanes, and alcohols + esters (+ acids)."
            "\n\n"
            "The measurements were all made at close to ambient conditions, and in "
            "almost all cases for three different compositions: 25%, 50% and 75%."
            "\n\n"
            "All of the systems present in this data set have corresponding enthalpy "
            "of mixing measurements in the `bmfs-exp-train-rho-x` data set. "
            "Furthermore, the densities and enthalpies of vaporization for each of "
            "the individual components in all of the binary mixtures can be found in "
            "the `bmfs-exp-train-rho` and `bmfs-exp-train-h-vap` data sets "
            "respectively."
            "\n\n"
            "This data set was originally curated for the `expanded` study as part of "
            "the `binary-mixture` project",
            authors=AUTHORS,
        ),
    ]

    return training_sets


def curate_pure_test_set(
    initial_data: pandas.DataFrame, training_data: List[DataSet]
) -> List[DataSet]:
    """Curate the test set of pure systems. This mostly contains hand
    curated enthalpy of vaporization measurements and density measurements
    made for the same systems.
    """
    sourced_h_vap_data = source_enthalpy_of_vaporization()
    sourced_components = {*sourced_h_vap_data["Component 1"].unique()}

    training_components = {
        data_entry.components[0].smiles
        for data_set in training_data
        for data_entry in data_set.entries
        if len(data_entry.components) == 1
    }

    test_components = sourced_components - training_components

    schema = CurationWorkflowSchema(
        component_schemas=[
            # Retain only enthalpy of vaporization and density data points
            # which were measured for the same pure systems.
            filtering.FilterByPropertyTypesSchema(
                property_types=["Density", "EnthalpyOfVaporization"],
                n_components={"Density": [1], "EnthalpyOfVaporization": [1]},
                strict=True,
            ),
            # Filter out all but the hand selected systems.
            filtering.FilterBySmilesSchema(smiles_to_include=[*test_components]),
            # Select data points close to ambient conditions
            selection.SelectDataPointsSchema(
                target_states=[
                    TargetState(
                        property_types=[("Density", 1), ("EnthalpyOfVaporization", 1)],
                        states=[
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(1.0,),
                            )
                        ],
                    )
                ]
            ),
        ],
    )

    # Apply the curation schema to yield the test set.
    test_data_frame = CurationWorkflow.apply(initial_data, schema, N_PROCESSES)

    rho_test_data = test_data_frame[test_data_frame["Density Value (g / ml)"].notna()]
    h_vap_test_data = test_data_frame[
        test_data_frame["EnthalpyOfVaporization Value (kJ / mol)"].notna()
    ]

    test_sets = [
        DataSet.from_pandas(
            data_frame=rho_test_data,
            identifier="bmfs-exp-test-rho",
            description="A data set composed of density measurements made for "
            "pure systems of alcohols, ethers, ketones, alkanes, and esters (+ acids). "
            "The measurements were all made at close to ambient conditions."
            "\n\n"
            "This data set was originally curated as part of the test set for the "
            "`expanded` study as part of the `binary-mixture` project",
            authors=AUTHORS,
        ),
        DataSet.from_pandas(
            data_frame=h_vap_test_data,
            identifier="bmfs-exp-test-h-vap",
            description="A data set composed of enthalpy of vaporization "
            "measurements made for pure systems of alcohols, ethers, ketones, "
            "alkanes, and esters (+ acids). The measurements were all made at close "
            "to ambient conditions."
            "\n\n"
            "This data set was originally curated as part of the test set for the "
            "`expanded` study as part of the `binary-mixture` project",
            authors=AUTHORS,
        ),
    ]

    return test_sets


def curate_mixture_test_set(
    initial_data: pandas.DataFrame, training_data: List[DataSet]
) -> List[DataSet]:
    """Curate the test set of mixture systems."""

    training_systems = {
        tuple(component.smiles for component in data_entry.components)
        for data_set in training_data
        for data_entry in data_set.entries
        if len(data_entry.components) == 2
    }

    schema = CurationWorkflowSchema(
        component_schemas=[
            # Attempt to inter-convert binary density and
            # excess molar volume data where possible.
            conversion.ConvertExcessDensityDataSchema(),
            # Remove any duplicate data.
            filtering.FilterDuplicatesSchema(),
            # Retain only enthalpy of mixing, density and excess molar volume
            # data points which were measured for the same binary systems.
            filtering.FilterByNComponentsSchema(n_components=[2]),
            filtering.FilterByPropertyTypesSchema(
                property_types=["Density", "EnthalpyOfMixing", "ExcessMolarVolume"],
            ),
            # Filter out the training systems.
            filtering.FilterBySubstancesSchema(
                substances_to_exclude=[*training_systems]
            ),
            # Filter out long chain molecules, 3 + 4 membered rings
            # and 1, 3 carbonyl compounds where one of the carbonyls
            # is a ketone (cases where the enol form may be present in
            # non-negligible amounts).
            filtering.FilterBySmirksSchema(
                smirks_to_exclude=[
                    # 3 + 4 membered rings.
                    "[#6r3]",
                    "[#6r4]",
                    # Long chain alkane /ether
                    "[#6,#8]~[#6,#8]~[#6,#8]~[#6,#8]~[#6,#8]~[#6,#8]~[#6,#8]~[#6,#8]",
                    # 1, 3 carbonyls with at least one ketone carbonyl.
                    "[#6](=[#8])-[#6](-[#1])(-[#1])-[#6](=[#8])-[#6]",
                ],
            ),
            # Filter out heavy water and carboxylic acids we wish to exclude from benchmarking
            # filtering.FilterBySmilesSchema(smiles_to_exclude=["[2H]O[2H]"]),
            filtering.FilterBySmilesSchema(smiles_to_exclude=["[2H]O[2H]", "CC(=O)O", "CCC(=O)O", "C(=O)O", "O=CO"]),

            # Filter out any racemic mixtures
            filtering.FilterByRacemicSchema(),
            # Attempt to select a diverse number of systems to include
            selection.SelectSubstancesSchema(
                target_environments=[
                    ChemicalEnvironment.Alcohol,
                    ChemicalEnvironment.CarboxylicAcidEster,
                    ChemicalEnvironment.Ether,
                    ChemicalEnvironment.Ketone,
                    ChemicalEnvironment.Alkane,
                ],
                n_per_environment=10,
                substances_to_exclude=[*training_systems],
                per_property=True,
            ),
            # Select data points close to ambient conditions
            selection.SelectDataPointsSchema(
                target_states=[
                    TargetState(
                        property_types=[
                            ("Density", 2),
                            ("EnthalpyOfMixing", 2),
                            ("ExcessMolarVolume", 2),
                        ],
                        states=[
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(0.25, 0.75),
                            ),
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(0.5, 0.5),
                            ),
                            State(
                                temperature=298.15,
                                pressure=101.325,
                                mole_fractions=(0.75, 0.25),
                            ),
                        ],
                    )
                ]
            ),
        ],
    )

    # Apply the curation schema to yield the test set.
    test_data_frame = CurationWorkflow.apply(initial_data, schema, N_PROCESSES)

    rho_x_test_data = test_data_frame[test_data_frame["Density Value (g / ml)"].notna()]
    h_mix_test_data = test_data_frame[
        test_data_frame["EnthalpyOfMixing Value (kJ / mol)"].notna()
    ]
    v_excess_test_data = test_data_frame[
        test_data_frame["ExcessMolarVolume Value (cm ** 3 / mol)"].notna()
    ]

    test_sets = [
        DataSet.from_pandas(
            data_frame=rho_x_test_data,
            identifier="bmfs-exp-test-rho-x",
            description="A data set composed of density measurements made for "
            "binary mixtures of alcohols, ethers, ketones, alkanes, and "
            "esters (+ acids)."
            "\n\n"
            "The measurements were all made at close to ambient conditions, and in "
            "almost all cases for three different compositions: 25%, 50% and 75%."
            "\n\n"
            "This data set was originally curated as part of the test set for the "
            "`expanded` study as part of the `binary-mixture` project",
            authors=AUTHORS,
        ),
        DataSet.from_pandas(
            data_frame=h_mix_test_data,
            identifier="bmfs-exp-test-h-mix",
            description="This data set is composed of enthalpy of mixing measurements "
            "made for binary mixtures of alcohols, ethers, ketones, alkanes, and "
            "esters (+ acids)."
            "\n\n"
            "The measurements were all made at close to ambient conditions, and in "
            "almost all cases for three different compositions: 25%, 50% and 75%."
            "\n\n"
            "This data set was originally curated as part of the test set for the "
            "`expanded` study as part of the `binary-mixture` project",
            authors=AUTHORS,
        ),
        DataSet.from_pandas(
            data_frame=v_excess_test_data,
            identifier="bmfs-exp-test-v-ex",
            description="This data set is composed of excess molar volume measurements "
            "made for binary mixtures of alcohols, ethers, ketones, alkanes, and "
            "esters (+ acids)."
            "\n\n"
            "The measurements were all made at close to ambient conditions, and in "
            "almost all cases for three different compositions: 25%, 50% and 75%."
            "\n\n"
            "This data set was originally curated as part of the test set for the "
            "`expanded` study as part of the `binary-mixture` project",
            authors=AUTHORS,
        ),
    ]

    return test_sets


def main():

    if not os.path.isfile("initial_data.csv"):

        initial_data = prepare_initial_data()
        # Save a copy of the initial data for faster restarts.
        initial_data.to_csv("initial_data.csv", index=False)

    initial_data = pandas.read_csv("initial_data.csv")

    training_sets: List[DataSet] = [
        *curate_pure_training_sets(initial_data),
        *curate_mixture_training_sets(initial_data),
    ]
    test_sets: List[DataSet] = [
        *curate_pure_test_set(initial_data, training_sets),
        *curate_mixture_test_set(initial_data, training_sets),
    ]

    # Save a copy of the curated data sets.
    os.makedirs("data-sets", exist_ok=True)

    for data_set in [*training_sets, *test_sets]:

        if UPLOAD:
            data_set = data_set.upload()

        data_set.to_pandas().to_csv(
            os.path.join("data-sets", f"{data_set.id}.csv"), index=False
        )
        data_set.to_file(os.path.join("data-sets", f"{data_set.id}.json"))


if __name__ == "__main__":
    main()
