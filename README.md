# [env_cleanup_utils](https://pypi.org/project/env-cleanup-utils/)

A Python package for cleaning up virtual environments (venv), `__pycache__`, and `node_modules` directories within a directory tree. It also saves the requirements of virtual environments to a `requirements.txt` file.
It is capable of traversing the subdirectories and finding all virtual environments

## Installation

You can install the `env_cleanup_utils` package using pip:

```bash
pip install env_cleanup_utils
```

## Usage

### Command Line Usage

You can use `env_cleanup_utils` as a command-line utility by running the following command:

```bash
python -m env_cleanup_utils [OPTIONS] ROOT_DIR
```

Replace `ROOT_DIR` with the root directory where you want to search for virtual environments.

#### Options:

- `--delete-all`: Delete venvs, `__pycache__`, and `node_modules` directories.
- `--delete-venv`: Delete virtual environments.
- `--delete-pycache`: Delete `__pycache__` directories (confirmed automatically).
- `--delete-node`: Delete `node_modules` directories.
- `-y`: Auto-confirm all deletion prompts.
- `--debug`: Enable debug mode for additional logging.

### Python API

You can also use `env_cleanup_utils` programmatically in your Python code. Import the necessary functions and classes from the package and call them as needed.

#### Example:

```python
from env_cleanup_utils import (
    find_venv_dirs,
    find_pycache_dirs,
    find_node_modules_dirs,
    save_requirements,
    delete_venv,
    delete_pycache,
    delete_node_modules,
)

# Use the functions and classes as needed.
```

## Sample Usage

```python
# Example command line usage:
python -m env_cleanup_utils ./my_project_directory --delete-venv --debug

# Example Python API usage:
from env_cleanup_utils import (
    find_venv_dirs,
    save_requirements,
    delete_venv,
)

root_dir = "./my_project_directory"
venv_dirs = find_venv_dirs(root_dir)

for venv_dir in venv_dirs:
    save_requirements(venv_dir)
    delete_venv(venv_dir)
```
## Contributing

If you would like to contribute to the development of the `env_cleanup_utils` package by adding more functionality, you are welcome to open a pull request.

## References
- [Github repository](https://github.com/t4skmanag3r/env_cleanup_utils)
- [PyPI package](https://pypi.org/project/env-cleanup-utils/)

---

Please ensure you have the required permissions before running the tool, and use it responsibly. This package is provided as-is, without any warranty or guarantee.
