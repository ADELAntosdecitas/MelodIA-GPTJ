# MelodIA GPT-J - RunPod Edition

Este proyecto ejecuta GPT-J 1.3 con Flask como backend y una interfaz básica.

## ¿Cómo usarlo?

```bash
pip install -r requirements.txt
bash start.sh
```

Accede a http://localhost:8989 o al puerto público en RunPod.

## Estructura

- `app.py`: servidor principal
- `scripts/gptj_server.py`: modelo GPT-J loader
- `frontend/`: HTML + CSS
- `logs/bitacora.txt`: para guardar respuestas
# trigger redeploy
