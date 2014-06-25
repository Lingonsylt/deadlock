FROM ubuntu:13.10
MAINTAINER Anton "anton@deadlock.se"

RUN apt-get update
RUN apt-get install -y build-essential python python-dev python-pip openssh-server supervisor
RUN pip install virtualenv uwsgi

EXPOSE 22
ADD public_key /root/.ssh/authorized_keys
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
RUN mkdir /var/run/sshd

ADD supervisor.conf /etc/supervisor/supervisord.conf
EXPOSE 8000

RUN virtualenv /etc/ve/deadlock_web
RUN mkdir -p /etc/apps/deadlock_web

ADD manage.py                /etc/apps/deadlock_web/
ADD requirements.txt         /etc/apps/deadlock_web/
ADD deadlock/                /etc/apps/deadlock_web/deadlock/
ADD blog/                    /etc/apps/deadlock_web/blog/
ADD ckeditor/                /etc/apps/deadlock_web/ckeditor/
ADD templates/               /etc/apps/deadlock_web/templates/
ADD static/                  /etc/apps/deadlock_web/static/
ADD local_settings_deploy.py /etc/apps/deadlock_web/deadlock/local_settings.py
ADD adminpass.txt            /etc/apps/deadlock_web/adminpass.txt

RUN /etc/ve/deadlock_web/bin/pip install -r /etc/apps/deadlock_web/requirements.txt
RUN (cd /etc/apps/deadlock_web/ && /etc/ve/deadlock_web/bin/python manage.py syncdb --noinput \
                                                                                    --settings=deadlock.local_settings)
RUN (cd /etc/apps/deadlock_web/ && /etc/ve/deadlock_web/bin/python manage.py collectstatic --noinput \
                                                                                    --settings=deadlock.local_settings)
RUN (cd /etc/apps/deadlock_web/ && echo "from django.contrib.auth.models import User;    \
    User.objects.create_superuser('anton', 'anton@deadlock.com', '`cat adminpass.txt`')" \
    | /etc/ve/deadlock_web/bin/python manage.py shell --settings=deadlock.local_settings)
RUN (cd /etc/apps/deadlock_web/ && rm adminpass.txt)

CMD ["supervisord", "-n"]