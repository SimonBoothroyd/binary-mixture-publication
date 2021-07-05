# Physical Property Data Sets

Within these directories are the scripts used to curate the experimental physical property
data sets that the LJ force field parameters were trained and tested (`benchmarks/`) against.

In particular:

* `source-h-vap-data.py` - contains the manually curated enthalpy of vaporization measurements.

* `curate-train-test-sets.py` - contains the automated workflows for building the train and test sets. This script
  is not intended to be deterministic and may yield slightly different sets if run multiple times. See the 
  `schemas/data-sets` directory for the **exact** data sets that were used.

All data sets were curated using the utilities provided by the `openff-evaluator` package and stored
for easy access in both `nonbonded` data set objects and pandas csv files.
