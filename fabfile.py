# encoding: utf-8
from fabric.api import *
import sys

sys.path.append("../dockctrl")
env.image_name = "deadlock/deadlock_web"
env.container_name = "deadlock_web"
env.appname = "deadlock_web"

from dockerfab import \
    buildimage, runimage, recreate_all, ls, \
    _remote_buildimage, remote_deploy, remote_runimage, pwd, \
    docker_ip, _local_fabric_key_check

def _gather_deploy():
    with hide():
        local("rm -rf deploy/")
    local("mkdir deploy/")
    for path in ('manage.py',
                 'requirements.txt',
                 'deadlock/',
                 'blog/',
                 'templates/'):
        local("cp -r %s deploy/" % path)
    env.deploy_pkg = "deploy/"

def _gather_dockerbuild():
    with hide():
        local("rm -rf dockerbuild/")
    local("mkdir dockerbuild/")
    for path in ('Dockerfile',
                 'supervisor.conf',
                 'fabfile.py',
                 '../dockctrl/dockerfab.py',
                 '../dockctrl/utils.py',
                 'sshdocker'):
        local("cp -r %s dockerbuild/" % path)
    env.dockerbuild_pkg = "dockerbuild/"

@hosts(docker_ip())
def deploy():
    env.user = "root"
    env.hosts = [docker_ip()]
    _local_fabric_key_check()
    with cd("/etc/apps/%s/" % env.appname):
        _gather_deploy()
        print "Uploading code..."
        with hide("running"):
            put(env.deploy_pkg, ".")
        print "Code uploaded!"
        local("rm -rf %s" % env.deploy_pkg)
        run("/etc/ve/%s/bin/pip install -r requirements.txt" % env.appname)
        run("/etc/ve/%s/bin/python manage.py syncdb --noinput" % env.appname)
        run("/etc/ve/%s/bin/python manage.py collectstatic --noinput" % env.appname)
        #run("/etc/ve/%s/bin/python manage.py migrate --all --noinput" % appname)
        run("supervisorctl restart %s" % env.appname)
        print "Deploy complete!"

def remote_buildimage():
    _gather_dockerbuild()
    _remote_buildimage()