# ucsf-query

This repository implements a simple python script to query the [UCSF Truth Tobacco Industry Documents Archive](https://www.industrydocuments.ucsf.edu/tobacco/). It will download all PDFs that match the search query.

## Setup

### System Requirements
This repository is primarily tested on Ubuntu 20.04 and macOS Monterey with Python 3.8.16.

### Installation
Python dependencies are managed with [Poetry](https://python-poetry.org/). If you'd like to use Poetry, please first follow its installation instructions [here](https://python-poetry.org/docs/). Otherwise, feel free to setup your Python virtual environment with e.g., Conda, Pipenv, or any alternative. 

Follow the installation procedure below to get setup:
```bash
# Clone repository.
git clone https://github.com/agiachris/ucsf-query.git
cd ucsf-query

# Install pyenv.
curl https://pyenv.run | bash 
exec $SHELL          # Restart shell for path changes to take effect.
pyenv install 3.8    # Install a Python version.
pyenv local 3.8      # Set Python 3.8 as default for local repository.

# If using Poetry, create venv.
poetry install       # Install Python dependencies.
poetry shell         # Activate virtual environment.

# Run the script.
# Ex: Querying for "Smoking and Health"
python main.py --query "Smoking and Health"
```

## Basic Usage
The only entry point is `main.py`! This script is easy to use, containing only a few flags shown below:
```bash
# After activating Poetry venv.
python main.py --query "<query>" --download-dir <download/path> --num-pages <N>
```

Here's what the script will do:
1. It will query the UCSF archive for all documents matching `"<query>"` 
2. By default, the script will download all matching documents to your `Downloads/UCSF_Industry_Documents` directory. However, you can use the flag `--download-dir <download/path>` to specify an alternative download directory.
3. By default, the UCSF server returns 100 documents per page. If `--num-pages` is not specified when calling `main.py`, the script will download the first page of documents (i.e., the first 100 PDFs). If you would like to download e.g., the first three pages of documents (i.e., 300 PDFs), use `--num-pages 3`.

## License
This repository is offered under the [MIT License](https://github.com/agiachris/ucsf-query/blob/main/LICENSE).