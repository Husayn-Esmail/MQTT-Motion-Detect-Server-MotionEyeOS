#!/bin/bash
source ../venv/bin/activate
export FLASK_DEBUG="True"
export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT="8085"
python3 -m flask run
