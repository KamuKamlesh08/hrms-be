@echo off
cd /d E:\HRMS\hrms-be

echo Cleaning...
rmdir /s /q .venv 2>nul
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
del /s /q *.pyc 2>nul

echo Creating venv...
python -m venv .venv
call .venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Starting server...
uvicorn app.main:app --reload