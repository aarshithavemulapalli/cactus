# CACTUS 🌵 | Chemistry Agent Connecting Tool Usage to Science
# Introduction 

CACTUS is an innovative tool-augmented language model designed to assist researchers and chemists in various chemistry-related tasks. By integrating state-of-the-art language models with a suite of powerful cheminformatics tools, CACTUS provides an intelligent and efficient solution for exploring chemical space, predicting molecular properties, and accelerating drug discovery. Just as the cactus thrives in the harsh desert environment, adapting to limited resources and extreme conditions, CACTUS has been implemented by Pacific Northwest National Laboratory (PNNL) Scientists to navigate the complex landscape of chemical data and extract valuable insights.

<img width="1000" alt="Cactus_header" src="assets/workflow_diagram_V2_white_bkg.png"> 


## Running Cactus 🏃

Getting started with Cactus is as simple as:

```python
from cactus.agent import Cactus

Model = Cactus(model_name="gpt-3.5-turbo", model_type="api")
Model.run("What is the molecular weight of the smiles: OCC1OC(O)C(C(C1O)O)O")
```
### or run the runcactus.py python file at terminal as
python runcactus.py
## Installation 💻

To install `cactus`:

```bash
pip install git+https://github.com/pnnl/cactus.git
```

The default `PyTorch` version is compiled for `cuda` 12.1 (or cpu for non-cuda systems). If you want to install for an older version of `cuda`, you should install from source and edit the `pyproject.toml` file at the `[[tool.rye.sources]]` section before installing. But be aware `vllm` may not work properly for older versions of `PyTorch`.

Note: `cactus` currently only supports Python versions `3.10`-`3.12`. Ensure you are using one of these versions before installation.

Alternatively for development, you can install in an editable configuration using:

```bash
git clone https://github.com/pnnl/cactus.git
cd cactus
python -m pip install -e .
```

or install using `rye` by running:

```bash
git clone https://github.com/pnnl/cactus.git
cd cactus
rye sync
```

## Benchmarking 📊

We provide scripts for generating lists of benchmarking questions to evaluate the performance of the CACTUS agent.

These scripts are located in the `benchmark` directory.

To build the dataset used in the paper, we can run:

```bash
python benchmark_creation.py
```

This will generate a readable dataset named `QuestionsChem.csv` for use with the `Cactus` agent.


## Tools Available

For the initial release, we have simple cheminformatics tools available:
| Tool Name                 | Tool Usage                                           |
|---------------------------|------------------------------------------------------|
| `calculate_molwt`         | Calculate Molecular weight                           |
| `calculate_logp`          | Calculate the Partition Coefficient                  |
| `calculate_tpsa`          | Calculate the Topological Polar Surface Area         |
| `calculate_qed`           | Calculate the Qualitative Estimate of Drug-likeness  |
| `calculate_sa`            | Calculate the Synthetic Accessibility                |
| `calculate_bbb_permeant`  | Calculate Blood Brain Barrier Permeance              |
| `calculate_gi_absorption` | Calculate the Gastrointestinal Absorption            |
| `calculate_druglikeness`  | Calculate druglikeness based on Lipinski's Rule of 5 |
| `brenk_filter`            | Calculate if molecule passes the Brenk Filter        |
| `pains_filter`            | Calculate if molecule passes the PAINS Filter        |

⚠️ Notice: These tools currently expect a SMILES as input, tools for conversion between identifiers are available but not yet working as intended. Fix to come soon.

