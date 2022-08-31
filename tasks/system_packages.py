from pyinfra.operations import apt, server

"""
    Installs the required system packages
"""

apt.packages(
    name="Ensure that micro zip and unzip packages are installed",
    packages=["micro", "unzip", "zip"],
    _sudo=True,
)
