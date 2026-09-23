# Maximo Automation Script Learning Repository

This repository provides a structured environment for learning and
testing IBM Maximo automation script concepts.

## Architecture

- `maximo_lib`: Reusable and locally testable business logic
- `automation_scripts`: Locally executable automation scripts
- `automation_scripts/maximo`: Maximo deployment scripts
- `automation_scripts/integration`: REST and integration examples
- `local_runtime`: Local simulations of Maximo runtime objects
- `tests`: Automated pytest tests
- `sample_data`: Sample asset and work order data
- `scripts`: General-purpose Python scripts
- `sql`: SQL learning examples
- `notebooks`: Jupyter and Google Colab notebooks
- `utilities`: Supporting utilities
- `docs`: Learning and deployment documentation

## Run all tests

Run this command from the repository root:

```bash
python -m pytest tests -v
```

## Run the asset example

```bash
python automation_scripts/asset_status_script.py
```

## Important

Files under `automation_scripts/maximo` require the actual Maximo
runtime and should not be imported into ordinary Python.

The local simulation does not reproduce every Maximo behavior.
All scripts must be tested in a development Maximo environment
before production deployment.

## Current learning topics

- Asset validation
- Asset status processing
- Work Order object launch points
- Attribute launch points
- Default Work Order priority
- Follow-up Work Order creation
- Maximo security group conditions
- MBO and MboSet simulations
- REST script examples
- Automated testing with pytest
