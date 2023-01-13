# Sideral Technologies - WSL2 Python Web Development Environment

This is a template for a Python web development environment in WSL2 developed by Sideral Technologies. It includes:

* pip - Python package manager
* virtualenv - Python virtual environment manager
* pipx - Python package manager for command line tools
* poetry - Python package manager and virtual environment manager
* mypy - Python static type checker
* micro - A modern and intuitive terminal-based text editor
* gh-cli (GitHub CLI) - GitHub command line tool
* oh-my-posh - A prompt theme for PowerShell (and other shells) 

This template is designed to provide a minimal, yet comprehensive development environment for Python web development projects. 

## Usage

To set up the environment, please run `./bootstrap.sh` in a clean Ubuntu container. The script will install the tools listed above and add them to your path. `gh` will require you to authenticate with GitHub. To do that, run `gh auth login` and follow the instructions.

For the sake of convenience, the script will also setup `gh` completion for `bash`. If you use another shell, you'll have to do that yourself.

## Why?

Sideral Technologies has developed this template to provide a minimal, yet comprehensive development environment for Python web development projects within WSL2. The template is designed to provide a clean environment that includes only the necessary tools and modules for development, allowing for easy management and scalability. Additionally, this template allows for the use of the same environment on both Windows and Linux machines.

### Why not just use a Docker container?

Sideral Technologies has determined that the use of a Docker container for the execution of Python scripts is not the most efficient solution. Instead, the template allows for direct execution of Python scripts from the command line for increased efficiency.

### Why not just use a virtual environment?

Sideral Technologies has determined that the use of a virtual environment for the execution of Python scripts is not the most efficient solution. Instead, the template allows for direct execution of Python scripts from the command line for increased efficiency.

### Why pyinfra and not Ansible?

Sideral Technologies has evaluated different configuration management tools and has determined that pyinfra is the most suitable for the needs of the company. Pyinfra is a lot simpler than Ansible and its written in Python, making it easier to understand and manage than Ansible's YAML

## Note

Please note that this template is intended for internal use only and should not be shared or distributed outside of Sideral Technologies. Unauthorized use of this script will result in severe disciplinary action, including termination of employment. Misuse of company resources will not be tolerated. If you have any questions or issues, please contact the IT department immediately.

## Disclaimer
Sideral Technologies will not be held responsible for any unauthorized or illegal use of this script. Use of this script is at your own risk and any consequences resulting from such use will be borne solely by the user.
