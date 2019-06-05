#!/bin/bash

# Author Apalya Technologies
# Date  31/05/2019
# Shell Script to fetch ip address of selenium grid and export the address so that python can use 
# it to launch the test

#set container name this can be viewed by executing docker-compose -ps
#use the name that belongs to selenium grid

#check if 2 arguments have been passed otherwise exit
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <browser> <script_name.py>\n" >&2
  echo "Usage: $0 firefox project/sunnxt.py\n" >&2
  exit 1
fi

sleep 3s #pause so that docker container is ready
CONTAINER="selenium-working_hub_1"
script_name=$2 #name of python script to execute
browser=$1 #which browser to test on ex: chrome or firefox


#get the ipaddress of selenium grid container
IP_ADDRESS=$(docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" $CONTAINER)

echo "Selenium grid is accessible at $IP_ADDRESS \n"
echo "Launching selenium test..... using $browser\n"

export BROWSER=$browser
export NODE_HUB_ADDRESS=$IP_ADDRESS

#launch python virtual environment
#virtualenv -p python3 venv

#activate the virtual environment
source venv/bin/activate

nohup python $script_name &
