from nonbonded.library.models.authors import Author
from nonbonded.library.models.projects import Project


def main():
    project = Project(
        id="binary-mixture",
        name="Binary Mixture Feasibility Study",
        description=(
            "In this study we aim to more rigorously understand whether it is more "
            "beneficial to optimize the non-bonded interaction parameters of a force "
            "field on solely pure data, binary mixture data, or a combination of both, "
            "with an emphasis here on density (including density , and excess molar "
            "volume) and enthalpy (including  enthalpy of vaporization  and enthalpy "
            "of mixing) data."
            "\n\n"
            "We anticipate that training a force field on mixture data will improve "
            "its performance at reproducing mixture properties while slightly "
            "degrading its performance on pure properties. Vice versa, we would expect "
            "that training on pure properties would improve its performance on pure "
            "properties while slightly degrading its performance on mixture "
            "properties. Here we aim to identify how much mixture properties improve "
            "relative to the degradation of pure properties when training on mixtures, "
            "compared to how much pure properties improve relative to the degradation "
            "of mixture properties when training on pure properties."
        ),
        authors=[
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
        ],
    )

    project.upload()


if __name__ == "__main__":
    main()
