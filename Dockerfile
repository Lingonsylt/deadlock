FROM ubuntu:13.10
MAINTAINER Anton "anton@deadlock.se"

RUN apt-get update
RUN apt-get install -y build-essential python python-dev python-pip openssh-server supervisor
RUN pip install fabric virtualenv uwsgi

EXPOSE 22
ADD fabric_rsa.pub /root/.ssh/authorized_keys
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
RUN mkdir /var/run/sshd

ADD supervisor.conf /etc/supervisor/supervisord.conf
EXPOSE 8000

RUN virtualenv /etc/ve/deadlock_web
RUN mkdir -p /etc/apps/deadlock_web

RUN sed -i 's/$PORT/8000/g' /etc/supervisor/supervisord.conf
RUN sed -i 's/$STATIC/\/etc\/apps\/deadlock_web\/static/g' /etc/supervisor/supervisord.conf
RUN sed -i 's/$VENV/\/etc\/ve\/deadlock_web/g' /etc/supervisor/supervisord.conf
RUN sed -i 's/$PROJ/deadlock/g' /etc/supervisor/supervisord.conf

CMD ["supervisord", "-n"]