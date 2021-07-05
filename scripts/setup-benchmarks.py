from typing import Any, Dict

from nonbonded.library.models.forcefield import ForceField
from nonbonded.library.models.projects import Benchmark
from nonbonded.library.utilities.environments import ChemicalEnvironment
from openff.toolkit.typing.engines import smirnoff

PROJECT_ID = "binary-mixture"
STUDY_ID = "expanded"


def common_benchmark_options() -> Dict[str, Any]:

    return dict(
        project_id=PROJECT_ID,
        study_id=STUDY_ID,
        test_set_ids=[
            "bmfs-exp-test-h-mix",
            "bmfs-exp-test-rho-x",
            "bmfs-exp-test-v-ex",
            "bmfs-exp-test-rho",
            "bmfs-exp-test-h-vap",
        ],
        analysis_environments=[
            ChemicalEnvironment.Alkane,
            ChemicalEnvironment.Alcohol,
            ChemicalEnvironment.CarboxylicAcidEster,
            ChemicalEnvironment.CarboxylicAcid,
            ChemicalEnvironment.Ether,
            ChemicalEnvironment.Ketone,
        ],
    )


def main():

    benchmarks = [
        Benchmark(
            id="h-mix-rho-x",
            name="Hmix(x) + rho(x)",
            description="A benchmark of the force field produced by the "
            "'h-mix-rho-x' optimization.",
            optimization_id="h-mix-rho-x",
            force_field=None,
            **common_benchmark_options(),
        ),
        Benchmark(
            id="h-mix-rho-x-rho",
            name="Hmix(x) + rho(x) + rho",
            description="A benchmark of the force field produced by the "
            "'h-mix-rho-x-rho' optimization.",
            optimization_id="h-mix-rho-x-rho",
            force_field=None,
            **common_benchmark_options(),
        ),
        Benchmark(
            id="h-mix-rho-x-rho-h-vap",
            name="Hmix(x) + rho(x) + rho + Hvap",
            description="A benchmark of the force field produced by the "
            "'h-mix-rho-x-rho-h-vap' optimization.",
            optimization_id="h-mix-rho-x-rho-h-vap",
            force_field=None,
            **common_benchmark_options(),
        ),
        Benchmark(
            id="rho-h-vap",
            name="rho + Hvap",
            description="A benchmark of the force field produced by the "
            "'rho-h-vap' optimization.",
            optimization_id="rho-h-vap",
            force_field=None,
            **common_benchmark_options(),
        ),
        Benchmark(
            id="openff-1-0-0",
            name="OpenFF 1.0.0",
            description="A benchmark against the openff-1.0.0 force field. This "
            "will server as a baseline given that it was used as the initial fitting "
            "parameters.",
            optimization_id=None,
            force_field=ForceField.from_openff(
                smirnoff.ForceField("openff-1.0.0.offxml")
            ),
            **common_benchmark_options(),
        ),
    ]

    for benchmark in benchmarks:
        benchmark.upload()


if __name__ == "__main__":
    main()
