#!/usr/bin/env bash
set -euo pipefail

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install coverage

echo "Compiling Python files (syntax check)..."
git ls-files "**/*.py" | xargs -r python -m py_compile || true

echo "Running tests with coverage..."
mkdir -p reports
coverage run --source=. manage.py test || true
coverage xml -o reports/coverage.xml || true

echo "Local CI finished. Reports in ./reports"
