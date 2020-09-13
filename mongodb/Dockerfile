FROM dubeyajit/ubuntu-gnuhealth:v01

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 4B7C549A058F8B6B

RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | tee /etc/apt/sources.list.d/mongodb.list

RUN mkdir -p /data/db

RUN apt update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt install -y mongodb-org

CMD [ "mongod", "--bind_ip_all" ]