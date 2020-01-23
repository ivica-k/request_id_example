#!/bin/bash
source ./venv/bin/activate

sed -i "s|self.app.config|app.config|g" ./venv/lib/python3.8/site-packages/flask_log_request_id/request_id.py

export FLASK_APP="app.py"
export FLASK_ENV="development"

flask run
