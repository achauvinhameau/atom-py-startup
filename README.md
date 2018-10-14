# atom & python & virtualenv & atom-script

How to start with python dev in atom with script running the programm in a virtualenv.

in atom, install the script package and set in the configure run option:
 * command = path to your python binary
 * command argument = {PROJECT_PATH}

in the environnement variable, you can set:
 * VIRTUALENV_PYTHON = link to python binary that will be used inside the virtualenv during the installation
 * VIRTUALENV_ENV = name of the virtual environment, env by default

more information in french on my site : https://xincto.me/2018/10/atom-script-python-et-virtualenv.html
