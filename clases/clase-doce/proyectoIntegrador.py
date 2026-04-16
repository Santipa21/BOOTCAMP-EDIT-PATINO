"""
proyectoIntegrador4.py - Etapa 4
Aplicación de escritorio con Tkinter basada en proyectoIntegrador3.py
"""

import tkinter as tk

# ── Diccionario de alumnos (equivalente al del proyecto 3) ──
alumnos = {}

# ── Ventana principal ────────────────────────────────────────
root = tk.Tk()
root.title("Sistema de Alumnos")
root.geometry("400x420")


# ════════════════════════════════════════════════════════════
#  FUNCIONES DE LAS OPCIONES DEL MENÚ
# ════════════════════════════════════════════════════════════

def opcion_1_agregar():
    """Solicita nombre y cursos, agrega el alumno al diccionario."""
    limpiar_area_dinamica()

    tk.Label(frame_dinamico, text="Nombre del alumno:").pack(pady=(10, 2))
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    tk.Label(frame_dinamico, text="Cantidad de cursos:").pack(pady=(8, 2))
    entry_cursos = tk.Entry(frame_dinamico)
    entry_cursos.pack()

    label_resultado = tk.Label(frame_dinamico, text="")
    label_resultado.pack(pady=6)

    def confirmar():
        nombre = entry_nombre.get().strip()
        cursos_raw = entry_cursos.get().strip()

        if not nombre or not cursos_raw:
            label_resultado.config(text="Por favor completá ambos campos.")
            return
        if not cursos_raw.isdigit():
            label_resultado.config(text="La cantidad de cursos debe ser un número entero.")
            return

        cantidad_cursos_alumno = int(cursos_raw)
        alumnos[nombre] = cantidad_cursos_alumno
        # Equivalente al print del proyecto 3
        print(f"El alumno {nombre} fue añadido a la lista con {cantidad_cursos_alumno} cursos.")
        label_resultado.config(text=f"Alumno {nombre} agregado con {cantidad_cursos_alumno} cursos.")

    tk.Button(frame_dinamico, text="Confirmar", command=confirmar).pack(pady=4)


def opcion_2_ver_lista():
    """Muestra la lista de alumnos. Equivalente al bloque elif operacion == '2'."""
    limpiar_area_dinamica()

    # Equivalente al print del proyecto 3
    print("Lista de alumnos:")
    tk.Label(frame_dinamico, text="Lista de alumnos:").pack(pady=(10, 4))

    if not alumnos:
        tk.Label(frame_dinamico, text="(La lista está vacía)").pack()
        print("(La lista está vacía)")
    else:
        for nombre, cursos in alumnos.items():
            print(f"{nombre} - {cursos} cursos.")
            tk.Label(frame_dinamico, text=f"{nombre} - {cursos} cursos.").pack()


def opcion_3_ver_cursos():
    """Solicita nombre y muestra cantidad de cursos. Equivalente al bloque elif operacion == '3'."""
    limpiar_area_dinamica()

    tk.Label(frame_dinamico, text="Nombre del alumno a buscar:").pack(pady=(10, 2))
    entry_buscar = tk.Entry(frame_dinamico)
    entry_buscar.pack()

    label_resultado = tk.Label(frame_dinamico, text="")
    label_resultado.pack(pady=6)

    def buscar():
        nombre_alumno = entry_buscar.get().strip()
        # Equivalente al if/else del proyecto 3
        if nombre_alumno in alumnos:
            msg = f"{nombre_alumno} está inscrito en {alumnos[nombre_alumno]} cursos."
        else:
            msg = "El alumno no se encuentra en la lista."
        print(msg)
        label_resultado.config(text=msg)

    tk.Button(frame_dinamico, text="Buscar", command=buscar).pack(pady=4)


def opcion_4_salir():
    """Termina la ejecución del programa. Equivalente al while operacion != '4'."""
    print("¡Gracias por utilizar el programa!")
    root.destroy()


# ════════════════════════════════════════════════════════════
#  FUNCIONES DE NAVEGACIÓN DE LA UI
# ════════════════════════════════════════════════════════════

def limpiar_area_dinamica():
    """Elimina todos los widgets del frame dinámico."""
    for widget in frame_dinamico.winfo_children():
        widget.destroy()


def mostrar_menu():
    """Muestra el menú principal con los 4 botones tras un login exitoso."""
    frame_login.pack_forget()
    frame_menu.pack(fill="x", padx=20, pady=10)
    frame_dinamico.pack(fill="both", expand=True, padx=20)


def intentar_login():
    """
    Valida usuario y contraseña.
    Equivalente al if/else de autenticación del proyecto 3.
    """
    nombre_usuario = entry_usuario.get().strip()
    clave_usuario  = entry_clave.get().strip()

    if nombre_usuario == "admin" and clave_usuario == "uni123":
        print("¡Bienvenido, admin!")
        mostrar_menu()
    else:
        # Equivalente al print del proyecto 3
        print("Usuario y/o contraseña incorrecta")
        label_error_login.config(text="Usuario y/o contraseña incorrecta")


# ════════════════════════════════════════════════════════════
#  CONSTRUCCIÓN DE LA INTERFAZ
# ════════════════════════════════════════════════════════════

# ── Frame de Login ───────────────────────────────────────────
frame_login = tk.Frame(root)
frame_login.pack(fill="x", padx=20, pady=30)

tk.Label(frame_login, text="Usuario:").grid(row=0, column=0, sticky="w", pady=4)
entry_usuario = tk.Entry(frame_login)
entry_usuario.grid(row=0, column=1, padx=8, pady=4)

tk.Label(frame_login, text="Contraseña:").grid(row=1, column=0, sticky="w", pady=4)
entry_clave = tk.Entry(frame_login, show="*")
entry_clave.grid(row=1, column=1, padx=8, pady=4)

tk.Button(frame_login, text="Ingresar", command=intentar_login).grid(
    row=2, column=0, columnspan=2, pady=10)

label_error_login = tk.Label(frame_login, text="", fg="red")
label_error_login.grid(row=3, column=0, columnspan=2)

# ── Frame del Menú (oculto hasta login exitoso) ──────────────
frame_menu = tk.Frame(root)

tk.Label(frame_menu, text="Ingrese el número de la operación que desea ejecutar:").pack(pady=(0, 6))

frame_botones = tk.Frame(frame_menu)
frame_botones.pack()

tk.Button(frame_botones, text="1 - Añadir un alumno a la lista",  width=30, command=opcion_1_agregar).grid(row=0, column=0, pady=2)
tk.Button(frame_botones, text="2 - Ver la lista de alumnos",       width=30, command=opcion_2_ver_lista).grid(row=1, column=0, pady=2)
tk.Button(frame_botones, text="3 - Ver cantidad de cursos",        width=30, command=opcion_3_ver_cursos).grid(row=2, column=0, pady=2)
tk.Button(frame_botones, text="4 - Salir",                         width=30, command=opcion_4_salir).grid(row=3, column=0, pady=2)

# ── Frame dinámico (cambia según la opción elegida) ──────────
frame_dinamico = tk.Frame(root)

# ── Arrancar la app ──────────────────────────────────────────
root.mainloop()