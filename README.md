Improved force field accuracy through training against physical properties of mixed systems 
===========================================================================================

This repository contains the scripts, inputs and the results generated as part of the *Improved force field accuracy 
through training against physical properties of mixed systems* publication.

### Structure

This repository is structured into four main directories:

* `data-set-curation` - contains the script used to curate the training and test data sets.

* `inputs-and-results` - contains the *most up to date* input files required to reproduce this study. **See the 
  Reproduction** section of this README for more information. The project structure was for the most part generated 
  automatically using the [`nonbonded`](https://github.com/SimonBoothroyd/nonbonded) package.
  
* `schema` - contains the [`nonbonded`](https://github.com/SimonBoothroyd/nonbonded) schemas which define the entirety 
  of the project, including definitions of the which optimizations and benchmarks to be performed and their respective 
  training and test data sets.
  
* `scripts` - contains the script used to curate the training and test data sets, generate the input 
  [`nonbonded`](https://github.com/SimonBoothroyd/nonbonded) schemas, and scripts which perform ancillary data analysis. 

### Experimental Data Sets

The experimental data sets used in this project were curated from the [NIST ThermoML](https://trc.nist.gov/ThermoML.html)
archive. The citations for the individual measurements can be found in `DATA-CITATIONS.bib` 

### Reproduction

The exact inputs used and outputs reported (including the conda environment used to generate them) in the publication  
have been included as tagged releases to this repository. 

For those looking to reproduce the study, the required dependencies may be obtained directly using conda:

```bash
conda env create --name binary-mixture-publication --file environment.yaml
```

#### Optimizations

In most cases the optimizations can be re-run using the following commands

```bash
cd inputs-and-results/optimizations/XXX/
nonbonded optimization run
nonbonded optimization analyze
```

where `XXX` is the unique mnemonic associated with a particular optimization.

#### Benchmarks

In most cases the benchmarks can be re-run using the following commands

```bash
cd inputs-and-results/benchmarks/XXX/
nonbonded optimization run
nonbonded optimization analyze
```

where `XXX` is the unique mnemonic associated with a particular benchmark.
