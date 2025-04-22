#!/bin/bash
echo "⚡ Cargando MelodIA GPT-J en producción..."
export FLASK_APP=scripts/gptj_server.py
flask run --host=0.0.0.0 --port=8989
