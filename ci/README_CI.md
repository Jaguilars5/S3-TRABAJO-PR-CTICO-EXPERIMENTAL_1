# CI local and GitHub Actions

Instrucciones rápidas:

- Workflow: [/.github/workflows/ci.yml](.github/workflows/ci.yml)
- Diagrama: [ci/ci_diagram.mmd](ci/ci_diagram.mmd)
- Script local (Linux/macOS): `ci/local_ci.sh`
- Script local (Windows PowerShell): `ci/local_ci.ps1`

Uso local (Linux/macOS):
```bash
bash ci/local_ci.sh > ci/ci_local_run.txt 2>&1
```

Uso local (Windows PowerShell):
```powershell
.\ci\local_ci.ps1 *> ci\ci_local_run.txt
```

Qué hace el pipeline:
- Instala dependencias desde `requirements.txt` y `coverage`.
- Compila todos los `.py` para verificar sintaxis.
- Ejecuta `manage.py test` bajo `coverage`.
- Genera `reports/coverage.xml` y lo sube como artifact en Actions.
