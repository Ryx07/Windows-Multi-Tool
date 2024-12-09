@echo off
NET SESSION >nul 2>&1
if %errorlevel% neq 0 (
    echo Non hai i privilegi di amministratore.
    echo Richiedendo i privilegi di amministratore...
    :: Esegui il batch come amministratore
    powershell -Command "Start-Process cmd -ArgumentList '/c, %~f0' -Verb runAs"
    exit /b
)

cd /d "%~dp0"

echo Eseguendo main.py come amministratore...
python main.py
pause
