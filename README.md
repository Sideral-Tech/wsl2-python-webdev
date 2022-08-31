# wsl2-python-webdev

This is a template for a Python web development environment in WSL2. It includes:

* pip - Python package manager
* virtualenv - Python virtual environment manager
* pipx - Python package manager for command line tools
* poetry - Python package manager and virtual environment manager
* mypy - Python static type checker
* micro - A modern and intuitive terminal-based text editor
* gh-cli (GitHub CLI) - https://cli.github.com/

No other tools or modules are installed. You can add them as you need them.

## Usage

Just run `./bootstrap.sh`, preferably in a clean Ubuntu container, and you're good to go. It will install the tools listed above and add them to your path. `gh` will require you to authenticate with GitHub. To do that, run `gh auth login` and follow the instructions.

For the sake of convenience, the script will also setup `gh` completion for `bash`. If you use another shell, you'll have to do that yourself.

## Why?

I wanted to have a Python web development environment in WSL2 that was as close to a "clean" environment as possible. I didn't want to install a bunch of tools and modules that I might not need. I also wanted to be able to use the same environment on my Windows machine and my Linux machine. This template is the result of that.

### Why not just use a Docker container?

Because I don't want to have to run a Docker container every time I want to run a Python script. I want to be able to run Python scripts directly from the command line.

### Why not just use a virtual environment?

Because I don't want to have to activate a virtual environment every time I want to run a Python script. I want to be able to run Python scripts directly from the command line. I've told you that just above.

### Why pyinfra and not Ansible?

Because I wanted to try pyinfra. I've used Ansible before and I like it, but I wanted to try something new. pyinfra is a lot simpler than Ansible and it's written in Python, so it's easier to understand than the mess that Ansible's YAML files are.
