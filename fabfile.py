# -*- coding: utf-8 -*-
"""
Usage:

    fab deploy
    fab rollback
"""

from fabric.api import *
from fabric.contrib import files
import datetime

env.user = 'vagrant'
env.password = 'vagrant'
env.hosts = '192.168.33.20'
env.colorize_errors = True

@task
def deploy():
    now = datetime.datetime.now()
    env.release = now.strftime('%Y-%m-%d-%H.%M.%S')

    with cd("/opt/site"):
        run("mkdir -p releases/%(release)s" % env)

    with cd("/opt/site/git"):
        run("git pull")
        run("git archive master | tar -x -C /opt/site/releases/%(release)s" % env)

    with cd("/opt/site"):
        if files.exists("previous"): run("rm previous")
        if files.exists("current"):
            run("cp -P current previous")
            run("ln -sfn releases/%(release)s current" % env)
        else:
            run("ln -s releases/%(release)s current" % env)

@task
def rollback():
    with cd("/opt/site"):
        run("rm current && mv previous current")

