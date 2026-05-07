@echo off
echo Установка PyInstaller...
pip install -r requirements.txt
echo Сборка .exe файла...
pyinstaller --onefile --windowed --name Calculator --clean calculator.py
echo Готово! Проверь папку dist\
pause