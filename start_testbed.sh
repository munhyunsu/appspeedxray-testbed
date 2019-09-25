#!/bin/bash
cd "$(dirname "$(realpath "$0")")";
source ./venv/bin/activate
FLASK_APP=start_testbed.py flask run --host=0.0.0.0 --port=8888
