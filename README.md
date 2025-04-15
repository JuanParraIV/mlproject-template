# End to End Machine Learning Project

## Overview
This repository provides a standardized template for machine learning projects with proper MLOps practices. It includes project structure, environment setup, and development workflows.

## Project Structure
```
mlproject-template/
├── Makefile            # Automation commands for project tasks
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── setup.py            # Package installation configuration
├── src/                # Source code directory
│   └── __init__.py     # Makes src a Python package
└── mlproject.egg-info/ # Package metadata (generated)
```

## Environment Setup

### Creating the Environment
This project uses Conda for environment management. To create a new environment:

```bash
make vcreate
```

This will create a conda environment with Python 3.12 in the `venv` directory.

### Activating the Environment
To activate the environment, you need to run:

```bash
conda activate /path/to/mlproject-template/venv
```

**Note**: The environment activation cannot be done directly through Make as it runs commands in separate subshells.

### Installing Dependencies
After activating the environment, install the dependencies with:

```bash
make install
```

## Development

### Package Structure
The project is set up as an installable Python package with `setup.py`, which makes importing modules easier and enables proper dependency management.

### Adding Dependencies
Add new dependencies to the `requirements.txt` file, then run `make install` to install them in your environment.

## Contribution Guidelines
- Ensure all code follows the project's style guidelines
- Write tests for new features
- Update documentation when necessary


## Contact
Juan Mario Parra
jmparra.dev@gmail.com

---

*This ML project template was last updated: April 15, 2025.*