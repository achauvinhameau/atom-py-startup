# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2018-02-28 21:14:46 alex>
#
# --------------------------------------------------------------------
# atom-py-startup init
# Copyright (C) 2016-2017  Alexandre Chauvin Hameau <ach@meta-x.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
 main module which loads virtualenv and init it if not existing
 once initialized the environnement, the main.py will be started
"""

import logging
import os
import sys

LOGGER = logging.getLogger('apscheduler.executors.default')
LOGGER.setLevel(logging.ERROR)

_logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'

logging.basicConfig(format=_logFormat, level=logging.INFO)


def execInEnv(envname="env", globals=None, locals=None):
    """ run the current program in a virtualenv """
    logging.info('running in virtualenv: '+envname)
    if globals is None:
        globals = {}
    filepath = envname + "/Scripts/activate_this.py"
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)


logging.info("python version: {}".format(sys.version))

env = "env"
if 'VIRTUALENV_ENV' in os.environ:
    env = os.environ['VIRTUALENV_ENV']

pythonPath = None
if 'VIRTUALENV_PYTHON' in os.environ:
    pythonPath = os.environ['VIRTUALENV_PYTHON']

cmd = None
if not os.path.isdir(env):
    # create the virtualenv and init pip from requirements
    cmd = "virtualenv "
    if pythonPath is not None:
        cmd += '-p '+pythonPath+" "
    cmd += env

    logging.info("create virtualenv "+env+", not existing yet")
    os.system(cmd)

# jump in the virtuel environment created
execInEnv(env)

# install libs if needed
if cmd is not None:
    if os.path.isfile("requirements.txt"):
        logging.info("install libraries from reqs")
        cmd = "pip install -r requirements.txt"
        os.system(cmd)

import main
