# Importamos las funciones `setup` y `Executable`
# de la biblioteca `cx_Freeze`.
from cx_Freeze import setup, Executable

# Definimos un diccionario con las opciones
# para construir el ejecutable.
build_exe_options = {
    "packages": ["flet", "torch"],
    "includes": ["sys"],
}

# Definimos la variable `base` como `None`, lo que indica
# que el ejecutable no es una aplicación de interfaz gráfica
# de usuario. Si el sistema operativo es Windows, entonces
# `base` se establece en `"Win32GUI"`.
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Llamamos a la función `setup` para construir el ejecutable.
setup(
    name="guifoo",
    version="0.1",
    description="Transcriber",
    options={"build_exe": build_exe_options},
    executables=[Executable("transcriber.py", base=base, icon="icon.ico")],
)
