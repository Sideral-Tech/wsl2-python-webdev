from typing import List
from pyinfra.operations import server

themes_config: List[str] = [
    "mkdir ~/.poshthemes",
    "wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip",
    "unzip ~/.poshthemes/themes.zip -d ~/.poshthemes",
    "chmod u+rw ~/.poshthemes/*.omp.*",
    "rm ~/.poshthemes/themes.zip"
]

server.shell(
    name="Download oh-my-posh",
    commands=["wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh"],
    _sudo=True
)

server.shell(
    name="Download oh-my-posh",
    commands=["chmod +x /usr/local/bin/oh-my-posh"],
    _sudo=True
)

server.shell(
    name="Setup oh-my-posh",
    commands=themes_config
)
