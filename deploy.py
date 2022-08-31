from pyinfra import local

# Install system packages

local.include('tasks/system_packages.py')

# Install python modules

local.include('tasks/python_modules.py')

# Setup oh-my-posh

local.include('tasks/shell_configuration.py')

# Setup gh cli

local.include('tasks/github_cli.py')