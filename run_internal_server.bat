@echo off
setlocal
cd /d "%~dp0"
set "VPY=%CD%\.sca_env\Scripts\python.exe"
if not exist "%VPY%" (
  echo Run run_app.bat once first.
  pause
  exit /b 1
)
echo Starting SCA internal server on port 8501...
"%VPY%" -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true --browser.gatherUsageStats false
