from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (320, 480)

BOTONES = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
]

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=5, **kwargs)

        self.pantalla = TextInput(
            text='0',
            font_size=36,
            halign='right',
            readonly=True,
            size_hint=(1, 0.25),
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
        )
        self.add_widget(self.pantalla)

        for fila in BOTONES:
            fila_layout = BoxLayout(spacing=5)
            for simbolo in fila:
                btn = Button(
                    text=simbolo,
                    font_size=24,
                    background_color=(0.2, 0.6, 1, 1) if simbolo == '=' else (0.25, 0.25, 0.25, 1),
                    background_normal='',
                )
                btn.bind(on_press=self.presionar)
                fila_layout.add_widget(btn)
            self.add_widget(fila_layout)

    def presionar(self, boton):
        texto = boton.text

        if texto == 'C':
            self.pantalla.text = '0'
        elif texto == '=':
            try:
                resultado = str(eval(self.pantalla.text))
                self.pantalla.text = resultado
            except Exception:
                self.pantalla.text = 'Error'
        else:
            if self.pantalla.text == '0':
                self.pantalla.text = texto
            else:
                self.pantalla.text += texto


class AppCalculadora(App):
    def build(self):
        self.title = 'Calculadora Kivy'
        return Calculadora()


if __name__ == '__main__':
    AppCalculadora().run()