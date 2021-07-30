#!/bin/bash
mypath="$(dirname "`readlink -f "$0"`")"
docker build -f $mypath/Dockerfile --force-rm -t my_python_cronjob:latest $mypath