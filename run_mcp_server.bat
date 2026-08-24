@echo off
setlocal
cd /d "%~dp0"
set "VPY=%CD%\.sca_env\Scripts\python.exe"
if not exist "%VPY%" (
  echo Run run_app.bat successfully once first.
  pause
  exit /b 1
)
"%VPY%" -c "import mcp" >nul 2>nul
if errorlevel 1 (
  echo Installing optional MCP package...
  "%VPY%" -m pip install "mcp>=1.9"
  if errorlevel 1 (
    echo MCP installation failed.
    pause
    exit /b 1
  )
)
set /p WB=Full path to SCA workbook: 
"%VPY%" sca_mcp_server.py --workbook "%WB%" --host 0.0.0.0 --port 8765
