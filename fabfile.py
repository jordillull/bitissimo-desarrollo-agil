# -*- coding: utf-8 -*-
"""
Examples:

    fab deploy
    fab rollback
"""

from fabric.api import *
from fabric.contrib import files
from time import time

env.user = 'www'
env.colorize_errors = True

@task
def deploy():
    env.release = time.strftime('%Y%m%d%H%M%S')

    with cd("/opt/site"):
        run("mkdir -p releases/%(date)s" % env)

    with cd("/opt/site/repo"):
        run("git pull")
        run("git export master | tar -x -C /opt/site/releases/%(date)s" % env)

    with cd("/opt/site"):
        if files.exists("previous") run("rm previous")
        if files.exists("current") run("cp -P current previous")
        run("ln -sfn releases/%(date)s current" % env)

@task
def rollback():
    with cd("/opt/site/releases"):
        run("rm current && mv previous current")

