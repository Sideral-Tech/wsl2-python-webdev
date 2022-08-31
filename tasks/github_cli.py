from typing import List
from pyinfra.operations import server, apt

github_cli_repo_config: List[str] = [
    "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg",
    "sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg",
    'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null'
]

server.shell(
    name="Setup gh cli repositories",
    commands=github_cli_repo_config,
    _sudo=True,
)

apt.packages(
    name="Ensure that gh cli is installed",
    packages=["gh"],
    _sudo=True,
)

server.shell(
    name="Setup gh completion",
    commands=["gh completion -s bash | sudo tee /etc/bash_completion.d/gh > /dev/null"],
    _sudo=True
)