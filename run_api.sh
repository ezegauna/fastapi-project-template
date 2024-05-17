#!/bin/sh
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d "env" ]; then
    source env/bin/activate
else
    exit 1
fi

uvicorn api.run:app "$@"
