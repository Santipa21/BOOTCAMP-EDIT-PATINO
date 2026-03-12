import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import math
import time


# ─────────────────────────────────────────────
#  Ventana principal
# ─────────────────────────────────────────────
class AppEjemplo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🐍 App Ejemplo – Tkinter")
        self.geometry("700x520")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")

        self._build_ui()

    # ── construcción de la interfaz ──────────────
    def _build_ui(self):
        # Título
        tk.Label(
            self,
            text="App de Ejemplo con Tkinter",
            font=("Helvetica", 18, "bold"),
            bg="#1e1e2e",
            fg="#cba6f7",
        ).pack(pady=(20, 5))

        tk.Label(
            self,
            text="Explora las distintas pestañas para ver funciones de tkinter",
            font=("Helvetica", 10),
            bg="#1e1e2e",
            fg="#a6adc8",
        ).pack(pady=(0, 15))

        # Notebook (pestañas)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "TNotebook",
            background="#1e1e2e",
            borderwidth=0,
        )
        style.configure(
            "TNotebook.Tab",
            background="#313244",
            foreground="#cdd6f4",
            padding=[12, 5],
            font=("Helvetica", 10, "bold"),
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", "#cba6f7")],
            foreground=[("selected", "#1e1e2e")],
        )

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        nb.add(self._tab_calculadora(nb), text="  🧮 Calculadora  ")
        nb.add(self._tab_lista(nb),       text="  📋 Lista de Tareas  ")
        nb.add(self._tab_reloj(nb),       text="  🕐 Reloj  ")
        nb.add(self._tab_colores(nb),     text="  🎨 Colores  ")

    # ── Pestaña 1 – Calculadora ──────────────────
    def _tab_calculadora(self, parent):
        frame = tk.Frame(parent, bg="#181825", padx=20, pady=20)

        tk.Label(frame, text="Calculadora Simple",
                 font=("Helvetica", 13, "bold"),
                 bg="#181825", fg="#89b4fa").grid(
            row=0, column=0, columnspan=3, pady=(0, 12))

        def make_entry(row, label, default=""):
            tk.Label(frame, text=label, bg="#181825", fg="#cdd6f4",
                     font=("Helvetica", 10)).grid(row=row, column=0, sticky="e", padx=6)
            var = tk.StringVar(value=default)
            e = tk.Entry(frame, textvariable=var, width=14,
                         bg="#313244", fg="#cdd6f4",
                         insertbackground="#cdd6f4",
                         font=("Helvetica", 11), relief="flat")
            e.grid(row=row, column=1, pady=4, padx=6)
            return var

        v_a = make_entry(1, "Número A:", "12")
        v_b = make_entry(2, "Número B:", "4")

        resultado_var = tk.StringVar(value="—")
        tk.Label(frame, text="Resultado:", bg="#181825", fg="#cdd6f4",
                 font=("Helvetica", 10)).grid(row=3, column=0, sticky="e", padx=6, pady=8)
        tk.Label(frame, textvariable=resultado_var, bg="#181825",
                 fg="#a6e3a1", font=("Helvetica", 13, "bold")).grid(
            row=3, column=1, sticky="w")

        def operar(op):
            try:
                a, b = float(v_a.get()), float(v_b.get())
                if op == "/" and b == 0:
                    raise ZeroDivisionError
                ops = {"+": a + b, "-": a - b, "×": a * b, "/": a / b}
                res = ops[op]
                resultado_var.set(f"{res:.6g}")
            except ZeroDivisionError:
                messagebox.showerror("Error", "División por cero.")
            except ValueError:
                messagebox.showerror("Error", "Ingresa números válidos.")

        btn_frame = tk.Frame(frame, bg="#181825")
        btn_frame.grid(row=4, column=0, columnspan=3, pady=10)
        for op in ["+", "-", "×", "/"]:
            tk.Button(
                btn_frame, text=op, width=5,
                command=lambda o=op: operar(o),
                bg="#cba6f7", fg="#1e1e2e",
                font=("Helvetica", 12, "bold"),
                relief="flat", cursor="hand2",
                activebackground="#b4befe",
            ).pack(side="left", padx=6)

        return frame

    # ── Pestaña 2 – Lista de Tareas ──────────────
    def _tab_lista(self, parent):
        frame = tk.Frame(parent, bg="#181825", padx=20, pady=20)

        tk.Label(frame, text="Lista de Tareas",
                 font=("Helvetica", 13, "bold"),
                 bg="#181825", fg="#89b4fa").pack(pady=(0, 10))

        entrada_var = tk.StringVar()
        fila = tk.Frame(frame, bg="#181825")
        fila.pack(fill="x")

        entry = tk.Entry(fila, textvariable=entrada_var, width=35,
                         bg="#313244", fg="#cdd6f4",
                         insertbackground="#cdd6f4",
                         font=("Helvetica", 11), relief="flat")
        entry.pack(side="left", ipady=4, padx=(0, 6))

        listbox = tk.Listbox(
            frame, bg="#313244", fg="#cdd6f4",
            selectbackground="#cba6f7", selectforeground="#1e1e2e",
            font=("Helvetica", 11), relief="flat",
            height=9, borderwidth=0,
        )

        def agregar(event=None):
            tarea = entrada_var.get().strip()
            if tarea:
                listbox.insert("end", f"  ☐  {tarea}")
                entrada_var.set("")

        def eliminar():
            sel = listbox.curselection()
            if sel:
                listbox.delete(sel[0])
            else:
                messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

        def completar():
            sel = listbox.curselection()
            if sel:
                texto = listbox.get(sel[0])
                if "☐" in texto:
                    listbox.delete(sel[0])
                    listbox.insert(sel[0], texto.replace("☐", "✔"))
                    listbox.itemconfig(sel[0], fg="#a6e3a1")

        entry.bind("<Return>", agregar)

        tk.Button(fila, text="Agregar", command=agregar,
                  bg="#a6e3a1", fg="#1e1e2e",
                  font=("Helvetica", 10, "bold"),
                  relief="flat", cursor="hand2",
                  activebackground="#94e2d5").pack(side="left")

        listbox.pack(fill="both", expand=True, pady=10)

        btn_row = tk.Frame(frame, bg="#181825")
        btn_row.pack()
        for txt, cmd, color in [
            ("✔ Completar", completar, "#89b4fa"),
            ("🗑 Eliminar",  eliminar,  "#f38ba8"),
        ]:
            tk.Button(btn_row, text=txt, command=cmd,
                      bg=color, fg="#1e1e2e",
                      font=("Helvetica", 10, "bold"),
                      relief="flat", cursor="hand2",
                      width=14).pack(side="left", padx=6)

        return frame

    # ── Pestaña 3 – Reloj digital ─────────────────
    def _tab_reloj(self, parent):
        frame = tk.Frame(parent, bg="#181825")

        tk.Label(frame, text="Reloj Digital",
                 font=("Helvetica", 13, "bold"),
                 bg="#181825", fg="#89b4fa").pack(pady=(20, 10))

        hora_var = tk.StringVar()
        fecha_var = tk.StringVar()

        tk.Label(frame, textvariable=hora_var,
                 font=("Courier", 52, "bold"),
                 bg="#181825", fg="#cba6f7").pack()

        tk.Label(frame, textvariable=fecha_var,
                 font=("Helvetica", 14),
                 bg="#181825", fg="#a6adc8").pack(pady=5)

        # Canvas con segundo indicador
        canvas = tk.Canvas(frame, width=200, height=200,
                           bg="#181825", highlightthickness=0)
        canvas.pack(pady=15)
        canvas.create_oval(10, 10, 190, 190,
                           outline="#313244", width=3)
        manecilla = canvas.create_line(100, 100, 100, 20,
                                       fill="#cba6f7", width=3,
                                       capstyle="round")

        dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
                 "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

        def actualizar():
            t = time.localtime()
            hora_var.set(time.strftime("%H:%M:%S", t))
            fecha_var.set(
                f"{dias[t.tm_wday]}, {t.tm_mday} de {meses[t.tm_mon - 1]} {t.tm_year}"
            )
            ang = math.radians(t.tm_sec * 6 - 90)
            x2 = 100 + 80 * math.cos(ang)
            y2 = 100 + 80 * math.sin(ang)
            canvas.coords(manecilla, 100, 100, x2, y2)
            frame.after(1000, actualizar)

        actualizar()
        return frame

    # ── Pestaña 4 – Colores ──────────────────────
    def _tab_colores(self, parent):
        frame = tk.Frame(parent, bg="#181825", padx=20, pady=20)

        tk.Label(frame, text="Mezcla de Colores RGB",
                 font=("Helvetica", 13, "bold"),
                 bg="#181825", fg="#89b4fa").pack(pady=(0, 10))

        preview = tk.Label(frame, text="  Vista previa  ",
                           bg="#ffffff", fg="#000000",
                           font=("Helvetica", 14, "bold"),
                           width=22, height=4, relief="flat")
        preview.pack(pady=8)

        sliders = {}
        for nombre, color_fg in [("Rojo", "#f38ba8"),
                                   ("Verde", "#a6e3a1"),
                                   ("Azul", "#89b4fa")]:
            fila = tk.Frame(frame, bg="#181825")
            fila.pack(fill="x", pady=2)
            tk.Label(fila, text=f"{nombre:6}", width=6,
                     bg="#181825", fg=color_fg,
                     font=("Helvetica", 10, "bold")).pack(side="left")
            var = tk.IntVar(value=128)
            sl = tk.Scale(fila, from_=0, to=255,
                          orient="horizontal", variable=var,
                          bg="#181825", fg=color_fg,
                          troughcolor="#313244",
                          highlightthickness=0,
                          length=350, showvalue=True,
                          command=lambda *_: actualizar_color())
            sl.pack(side="left")
            sliders[nombre] = var

        hex_var = tk.StringVar(value="#808080")
        tk.Label(frame, textvariable=hex_var,
                 bg="#181825", fg="#cdd6f4",
                 font=("Courier", 11)).pack(pady=4)

        def actualizar_color():
            r = sliders["Rojo"].get()
            g = sliders["Verde"].get()
            b = sliders["Azul"].get()
            color = f"#{r:02x}{g:02x}{b:02x}"
            hex_var.set(color)
            preview.configure(bg=color)
            # contraste automático
            luminance = 0.299*r + 0.587*g + 0.114*b
            preview.configure(fg="#000000" if luminance > 128 else "#ffffff")

        def elegir_color():
            color = colorchooser.askcolor(title="Elige un color")[0]
            if color:
                r, g, b = (int(c) for c in color)
                sliders["Rojo"].set(r)
                sliders["Verde"].set(g)
                sliders["Azul"].set(b)
                actualizar_color()

        tk.Button(frame, text="🎨 Abrir selector de color",
                  command=elegir_color,
                  bg="#cba6f7", fg="#1e1e2e",
                  font=("Helvetica", 10, "bold"),
                  relief="flat", cursor="hand2",
                  activebackground="#b4befe").pack(pady=8)

        actualizar_color()
        return frame


# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = AppEjemplo()
    app.mainloop()