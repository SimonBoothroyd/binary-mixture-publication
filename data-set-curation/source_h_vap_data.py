"""This script collates all of the hand sourced enthalpy of vaporization data."""
import pandas
from nonbonded.library.models.datasets import Component, DataSetEntry
from openff.evaluator import substances


def source_enthalpy_of_vaporization() -> pandas.DataFrame:
    """Returns a list of hand sourced enthalpy of vaporization data
    entries"""

    data_entries = [
        # Formic Acid
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="OC=O", mole_fraction=1.0)],
            value=46.3,
            std_error=0.25,
            doi="10.3891/acta.chem.scand.24-2612",
        ),
        # Acetic Acid
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(O)=O", mole_fraction=1.0)],
            value=51.6,
            std_error=0.75,
            doi="10.3891/acta.chem.scand.24-2612",
        ),
        # Propionic Acid
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCC(O)=O", mole_fraction=1.0)],
            value=55,
            std_error=1,
            doi="10.3891/acta.chem.scand.24-2612",
        ),
        # Butyric Acid
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCC(O)=O", mole_fraction=1.0)],
            value=58,
            std_error=2,
            doi="10.3891/acta.chem.scand.24-2612",
        ),
        # Isobutyric Acid
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)C(O)=O", mole_fraction=1.0)],
            value=53,
            std_error=2,
            doi="10.3891/acta.chem.scand.24-2612",
        ),
        # Methanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CO", mole_fraction=1.0)],
            value=37.83,
            std_error=0.11349,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # Ethanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCO", mole_fraction=1.0)],
            value=42.46,
            std_error=0.12738,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # 1-Propanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCO", mole_fraction=1.0)],
            value=47.5,
            std_error=0.1425,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # Isopropanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)O", mole_fraction=1.0)],
            value=45.48,
            std_error=0.13644,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # n-Butanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCO", mole_fraction=1.0)],
            value=52.42,
            std_error=0.15726,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # Isobutanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)CO", mole_fraction=1.0)],
            value=50.89,
            std_error=0.15267,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # t-butanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)(C)O", mole_fraction=1.0)],
            value=46.75,
            std_error=0.14025,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # n-pentanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCO", mole_fraction=1.0)],
            value=44.36,
            std_error=0.13308,
            doi="10.1016/0378-3812(85)90026-3",
        ),
        # 1-hexanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCCO", mole_fraction=1.0)],
            value=61.85,
            std_error=0.2,
            doi="10.1016/0021-9614(77)90202-6",
        ),
        # 1-heptanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCCCO", mole_fraction=1.0)],
            value=66.81,
            std_error=0.2,
            doi="10.1016/0021-9614(77)90202-6",
        ),
        # 1-octanol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCCCCO", mole_fraction=1.0)],
            value=70.98,
            std_error=0.42,
            doi="10.1016/0021-9614(77)90202-6",
        ),
        # Propyl formate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCOC=O", mole_fraction=1.0)],
            value=37.49,
            std_error=0.07498,
            doi="10.1135/cccc19803233",
        ),
        # Butyl formate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCOC=O", mole_fraction=1.0)],
            value=41.25,
            std_error=0.0825,
            doi="10.1135/cccc19803233",
        ),
        # Methyl acetate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="COC(C)=O", mole_fraction=1.0)],
            value=32.3,
            std_error=0.0646,
            doi="10.1135/cccc19803233",
        ),
        # Ethyl acetate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCOC(C)=O", mole_fraction=1.0)],
            value=35.62,
            std_error=0.07124,
            doi="10.1135/cccc19803233",
        ),
        # Propyl acetate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCOC(C)=O", mole_fraction=1.0)],
            value=39.83,
            std_error=0.07966,
            doi="10.1135/cccc19803233",
        ),
        # Methyl propionate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCC(=O)OC", mole_fraction=1.0)],
            value=35.85,
            std_error=0.0717,
            doi="10.1135/cccc19803233",
        ),
        # Ethyl propionate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCOC(=O)CC", mole_fraction=1.0)],
            value=39.25,
            std_error=0.0785,
            doi="10.1135/cccc19803233",
        ),
        # Butyl acetate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=313.5,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCOC(C)=O", mole_fraction=1.0)],
            value=42.96,
            std_error=0.08592,
            doi="10.1135/cccc19803233",
        ),
        # Propyl propionate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=313.5,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCOC(=O)CC", mole_fraction=1.0)],
            value=42.14,
            std_error=0.08428,
            doi="10.1135/cccc19803233",
        ),
        # Methyl Butanoate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCC(=O)OC", mole_fraction=1.0)],
            value=40.1,
            std_error=0.4,
            doi="10.1007/BF00653098",
        ),
        # Methyl Pentanoate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCC(=O)OC", mole_fraction=1.0)],
            value=44.32,
            std_error=0.5,
            doi="10.1007/BF00653098",
        ),
        # Ethyl Butanoate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCC(=O)OCC", mole_fraction=1.0)],
            value=42.86,
            std_error=0.1,
            doi="10.1016/0021-9614(86)90070-4",
        ),
        # Ethylene glycol diacetate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(=O)OCCOC(=O)C", mole_fraction=1.0)],
            value=61.44,
            std_error=0.15,
            doi="10.1016/0021-9614(86)90070-4",
        ),
        # Methyl formate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=293.25,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="COC=O", mole_fraction=1.0)],
            value=28.7187400224,
            std_error=None,
            doi="10.1135/cccc19760001",
        ),
        # Ethyl formate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=304,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCOC=O", mole_fraction=1.0)],
            value=31.63314346416,
            std_error=None,
            doi="10.1135/cccc19760001",
        ),
        # 1,3-propanediol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="OCCCO", mole_fraction=1.0)],
            value=70.5,
            std_error=0.3,
            doi="10.1021/je060419q",
        ),
        # 2,4 pentanediol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(CC(C)O)O", mole_fraction=1.0)],
            value=72.5,
            std_error=0.3,
            doi="10.1021/je060419q",
        ),
        # glycerol
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="C(C(CO)O)O", mole_fraction=1.0)],
            value=91.7,
            std_error=0.9,
            doi="10.1016/0021-9614(88)90173-5",
        ),
        # Diethyl Malonate
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCOC(=O)CC(=O)OCC", mole_fraction=1.0)],
            value=61.70,
            std_error=0.25,
            doi="10.1021/je100231g",
        ),
        # 1,4-dioxane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="C1COCCO1", mole_fraction=1.0)],
            value=38.64,
            std_error=0.05,
            doi="10.1039/P29820000565",
        ),
        # oxane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="C1CCOCC1", mole_fraction=1.0)],
            value=34.94,
            std_error=0.84,
            doi="10.1039/TF9615702125",
        ),
        # methyl tert butyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="COC(C)(C)C", mole_fraction=1.0)],
            value=32.42,
            std_error=None,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # diisopropyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)OC(C)C", mole_fraction=1.0)],
            value=32.12,
            std_error=None,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # Dibutyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCOCCCC", mole_fraction=1.0)],
            value=44.99,
            std_error=None,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # cyclopentanone
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.16,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="O=C1CCCC1", mole_fraction=1.0)],
            value=42.63,
            std_error=0.42,
            doi="10.1002/hlca.19720550510",
        ),
        # 2-pentanone
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCC(C)=O", mole_fraction=1.0)],
            value=38.43,
            std_error=None,
            doi="10.1016/0021-9614(83)90091-5",
        ),
        # cyclohexanone
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.16,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="O=C1CCCCC1", mole_fraction=1.0)],
            value=44.89,
            std_error=0.63,
            doi="10.1002/hlca.19720550510",
        ),
        # cycloheptanone
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.16,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="O=C1CCCCCC1", mole_fraction=1.0)],
            value=49.54,
            std_error=0.63,
            doi="10.1002/hlca.19720550510",
        ),
        # cyclohexane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="C1CCCCC1", mole_fraction=1.0)],
            value=33.02,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # hexane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCC", mole_fraction=1.0)],
            value=31.55,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # methylcyclohexane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC1CCCCC1", mole_fraction=1.0)],
            value=35.38,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # heptane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCCC", mole_fraction=1.0)],
            value=36.58,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # iso-octane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)CC(C)(C)C", mole_fraction=1.0)],
            value=35.13,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # decane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCCCCCC", mole_fraction=1.0)],
            value=51.35,
            std_error=None,
            doi="10.3891/acta.chem.scand.20-0536",
        ),
        # acetone
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=300.4,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(C)=O", mole_fraction=1.0)],
            value=30.848632,
            std_error=0.008368,
            doi="10.1021/ja01559a015",
        ),
        # butan-2-one
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCC(C)=O", mole_fraction=1.0)],
            value=34.51,
            std_error=0.04,
            doi="0021-9614(79)90127-7",
        ),
        # pentan-3-one
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCC(=O)CC", mole_fraction=1.0)],
            value=38.52,
            std_error=None,
            doi="10.1016/0021-9614(83)90091-5",
        ),
        # 4-methylpentan-2-one
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CC(=O)CC(C)C", mole_fraction=1.0)],
            value=40.56,
            std_error=None,
            doi="10.1016/0021-9614(83)90091-5",
        ),
        # 3-hexanone
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCC(=O)CC", mole_fraction=1.0)],
            value=42.45,
            std_error=None,
            doi="10.1016/0021-9614(83)90091-5",
        ),
        # 2-methylheptane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCC(C)C", mole_fraction=1.0)],
            value=39.66,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # 3-methylpentane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCC(C)CC", mole_fraction=1.0)],
            value=30.26,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # 2-Methylhexane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCC(C)C", mole_fraction=1.0)],
            value=34.85,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # Octane
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCCCCC", mole_fraction=1.0)],
            value=41.47,
            std_error=None,
            doi="10.1135/cccc19790637",
        ),
        # Methyl Propyl Ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCOC", mole_fraction=1.0)],
            value=27.57,
            std_error=0.068925,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # Ethyl isopropyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCOC(C)C", mole_fraction=1.0)],
            value=30.04,
            std_error=0.0751,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # Dipropyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCOCCC", mole_fraction=1.0)],
            value=35.68,
            std_error=0.0892,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # butyl methyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="CCCCOC", mole_fraction=1.0)],
            value=32.43,
            std_error=0.081075,
            doi="10.1016/0021-9614(80)90152-4",
        ),
        # methyl isopropyl ether
        DataSetEntry(
            property_type="EnthalpyOfVaporization",
            temperature=298.15,
            pressure=101.325,
            phase="Liquid + Gas",
            components=[Component(smiles="COC(C)C", mole_fraction=1.0)],
            value=26.41,
            std_error=0.066025,
            doi="10.1016/0021-9614(80)90152-4",
        ),
    ]

    # Normalize the smiles patterns.
    for data_entry in data_entries:

        original_smiles = data_entry.components[0].smiles
        normalized_smiles = substances.Component(original_smiles).smiles

        data_entry.components[0].smiles = normalized_smiles

    data_rows = [data_entry.to_series() for data_entry in data_entries]
    data_frame = pandas.DataFrame(data_rows)

    return data_frame
