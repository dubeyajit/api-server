#!/bin/bash

if [ "$EUID" != "0" ]; then
    echo "Running script with root privileges"
	exec sudo bash $0 $@
fi

docker rm -f mongo-db-server
echo
echo ==== Building Production Tool Docker image
echo

docker build -t mngdbs . $@