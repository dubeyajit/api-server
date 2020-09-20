FROM ubuntu:20.04

LABEL Description=" Creating image for Python Flask Project"

RUN apt update

RUN apt install -y libldap2-dev rng-tools libbz2-dev zlib1g-dev libsqlite3-dev libreadline-dev pcscd scdaemon
RUN apt install -y make wget file pinentry-tty ca-certificates lbzip2 bzip2 gcc nano
RUN apt clean

RUN apt-get update && apt-get install -y --no-install-recommends gzip curl ca-certificates
RUN apt-get install -y python3-pip

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-pip 2to3 unoconv vim
RUN pip3 install --user chardet python-dateutil simplejson Flask-Bcrypt

# Further to add for flask project
RUN pip3 install flask Flask-PyMongo pipenv

WORKDIR /projects/Flask_Blog/
#RUN pipenv flask flask-pymongo python-dotenv

#ENV FLASK_APP=flaskblog.py 
#RUN flask run

EXPOSE 5000

# Set the default command to run when starting
#CMD [ "flask", "run" ]
CMD ["bash"]
#CMD ["flask", "run"]