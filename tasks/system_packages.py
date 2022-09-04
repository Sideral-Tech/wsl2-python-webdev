from pyinfra.operations import apt, server

"""
    Installs the required system packages
"""

apt.packages(
    name="Ensure that required system packages are installed",
    packages=["micro", "unzip", "zip", "build-essential", "python3-dev"],
    _sudo=True,
)
