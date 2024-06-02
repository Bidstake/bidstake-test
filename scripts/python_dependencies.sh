#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/bidstake-test/requirements.txt

#!/bin/bash

set -e

log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1"
}

log "Updating package list"
sudo apt-get update || { log "Failed to update package list"; exit 1; }

log "Installing MySQL client development libraries"
sudo apt-get install -y libmysqlclient-dev || { log "Failed to install MySQL client libraries"; exit 1; }

log "Installing pkg-config"
sudo apt-get install -y pkg-config || { log "Failed to install pkg-config"; exit 1; }

log "Installing build-essential and python3-dev"
sudo apt-get install -y build-essential python3-dev || { log "Failed to install build-essential or python3-dev"; exit 1; }

log "Setting environment variables for MySQL client"
MYSQLCLIENT_CFLAGS=$(mysql_config --cflags) || { log "Failed to get MYSQLCLIENT_CFLAGS"; exit 1; }
export MYSQLCLIENT_CFLAGS
MYSQLCLIENT_LDFLAGS=$(mysql_config --libs) || { log "Failed to get MYSQLCLIENT_LDFLAGS"; exit 1; }
export MYSQLCLIENT_LDFLAGS

log "Environment variables set: MYSQLCLIENT_CFLAGS=$MYSQLCLIENT_CFLAGS, MYSQLCLIENT_LDFLAGS=$MYSQLCLIENT_LDFLAGS"

log "Installing Python dependencies"
pip install -r requirements.txt || { log "Failed to install Python dependencies"; exit 1; }

log "Script completed successfully"
