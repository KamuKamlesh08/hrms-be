@echo off
cd /d E:\HRMS\hrms-be

echo =========================
echo Cleaning project...
echo =========================

echo Removing virtual environment...
rmdir /s /q .venv 2>nul

echo Removing __pycache__ folders...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo Removing .pyc files...
del /s /q *.pyc 2>nul

echo Removing .pytest_cache...
rmdir /s /q .pytest_cache 2>nul

echo Removing .mypy_cache...
rmdir /s /q .mypy_cache 2>nul

echo Removing .ruff_cache...
rmdir /s /q .ruff_cache 2>nul

echo Cleaning done successfully!
echo =========================
pause