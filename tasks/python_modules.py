from pyinfra.operations import server, pip

pip.packages(
    name="Ensure mypy module is installed",
    packages=["mypy>=0.971"],
    virtualenv=None
)

server.shell(
    name="Install poetry",
    commands=["pipx install poetry"]
)