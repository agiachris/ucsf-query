# ucsf-query

This repository implements a simple python script to query the [UCSF Truth Tobacco Industry Documents Archive](https://www.industrydocuments.ucsf.edu/tobacco/).

## Setup

### System Requirements
This repository is primarily tested on Ubuntu 20.04 and macOS Monterey with Python 3.8.16.

### Installation
Python dependencies are managed with Poetry. If you'd like to use Poetry, please follow the [installation instructions](https://python-poetry.org/docs/). Otherwise, please feel free to setup your Python virtual environment with e.g., Conda, Pipenv, or any `venv` alternative. 

Follow the installation procedure below to get setup:

```bash
# Install pyenv.
curl https://pyenv.run | bash 
exec $SHELL          # Restart shell for path changes to take effect.
pyenv install 3.8    # Install a Python version.
pyenv local 3.8      # Set Python 3.8 as default for local repository.

# Clone repository.
git clone https://github.com/agiachris/ucsf-query.git
cd ucsf-query

# Create Poetry venv.
poetry install       # Install Python dependencies.
poetry shell         # Activate virtual environment.

# Run the script.
# Ex: Querying for "Smoking and Health"
python main.py --query "Smoking and Health"
```

## Basic Usage
The only entry point is `main.py`! This script is easy to use, containing only a few flags as shown below:
```bash
# After activating Poetry venv.
python main.py --query "<query>" --download-dir <download/path> --num-pages <N>
```

This script will achieve the following:
1. It will query the UCSF archive for all documents matching `"<query>"` 
2. It will download matching documents to the specified download directory `<download/path>`
3. By default, the UCSF server returns 100 documents per page. If `--num-pages` is not specified when calling `main.py`, the script will download the first page of document (i.e., the first 100 PDFs). If you would like to download e.g., the first three pages of document (i.e., 300 PDFs), use `--num-pages 3`.

## License
This repository is offered under the [MIT License](https://github.com/agiachris/ucsf-query/blob/main/LICENSE).