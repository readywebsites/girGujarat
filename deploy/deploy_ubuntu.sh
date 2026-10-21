#!/bin/bash
# ==============================================================================
# TRAVEL FIRST HOLIDAYS — PRODUCTION APPLICATION UPDATE SCRIPT
# Execute on Ubuntu VPS as 'girapp' user inside /srv/girgujarat:
#   bash deploy/deploy_ubuntu.sh
# ==============================================================================

set -e

PROJECT_DIR="/srv/girgujarat"
BACKEND_DIR="${PROJECT_DIR}/backend"
VENV_DIR="${PROJECT_DIR}/.venv"

echo ">>> [1/4] Navigating to project directory: ${PROJECT_DIR}"
cd "${PROJECT_DIR}"

echo ">>> [2/4] Pulling latest code from GitHub..."
git pull origin main

echo ">>> [3/4] Installing / verifying dependencies..."
source "${VENV_DIR}/bin/activate"
pip install -r requirements.txt

echo ">>> [4/4] Applying database migrations & collecting static files..."
cd "${BACKEND_DIR}"
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "====================================================================="
echo " Application code and database migrations updated successfully!"
echo " Next: Reload Gunicorn service from your admin/sudo account:"
echo "   sudo systemctl reload girgujarat"
echo "====================================================================="
