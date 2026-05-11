Write-Host "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install coverage

Write-Host "Compiling Python files (syntax check)..."
git ls-files "**/*.py" | ForEach-Object { python -m py_compile $_ } -ErrorAction SilentlyContinue

Write-Host "Running tests with coverage..."
New-Item -ItemType Directory -Force -Path reports | Out-Null
Start-Process -NoNewWindow -Wait -FilePath python -ArgumentList "-m","coverage","run","--source=.","manage.py","test"
Start-Process -NoNewWindow -Wait -FilePath python -ArgumentList "-m","coverage","xml","-o","reports/coverage.xml"

Write-Host "Local CI finished. Reports in .\reports"
