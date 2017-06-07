#!/bin/bash

# Prepare log files and start outputting logs to stdout
#touch /srv/logs/gunicorn.log
#touch /srv/logs/access.log
#tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
#echo Starting Gunicorn.
exec gunicorn config.wsgi:application \
    --name v-user \
    --bind 0.0.0.0:80 \
    --workers 3 \
    --log-level=info \
    "$@"
