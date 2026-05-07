# Windows Calculator GUI

Простой графический калькулятор для Windows 10/11 на Python + Tkinter.

## 🚀 Как получить .exe файл

### Самый простой способ:
1. Установи Python (с галочкой **Add python.exe to PATH**)
2. Скачай репозиторий
3. Дважды кликни по `build_exe.bat`

.exe появится в папке `dist/Calculator.exe`

## Ручная команда:
```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name Calculator calculator.py
```

Готовый файл — **Calculator.exe** (один файл, без установки Python)