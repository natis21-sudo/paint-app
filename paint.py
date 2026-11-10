# -*- coding: utf-8 -*-
# ==========================================
# PROYECTO FINAL: BOCETO DE PAINT (ENTREGA 2)
# Nota de uso de IA: Este bloque de código lógico
# fue estructurado con apoyo de Inteligencia Artificial
# cumpliendo la norma del curso, para simular las
# funciones base del Paint (dibujar con 4 colores).
# ==========================================

import tkinter as tk

# Los 4 colores básicos disponibles
COLORES = {
    "Negro": "black",
    "Rojo": "red",
    "Azul": "blue",
    "Verde": "green",
    "Morado" : "purple",
    "Naranja" : "orange"
}

GROSOR_LAPIZ = 4      # tamaño del lápiz
GROSOR_BORRADOR = 20  # tamaño del borrador
COLOR_FONDO = "white"


class Paint:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Boceto de Paint")
        self.color_actual = "black"
        self.grosor_actual = GROSOR_LAPIZ
        self.ultimo_x = None
        self.ultimo_y = None

        # Barra superior con los botones de colores
        barra = tk.Frame(ventana)
        barra.pack(side="top", fill="x")
        tk.Label(barra, text="Color:").pack(side="left", padx=5)

        for nombre, codigo in COLORES.items():
            boton = tk.Button(
                barra,
                text=nombre,
                bg=codigo,
                fg="white",
                width=8,
                command=lambda c=codigo: self.cambiar_color(c),
            )
            boton.pack(side="left", padx=2, pady=4)

        # Botón del borrador
        tk.Button(
            barra,
            text="Borrador",
            width=8,
            command=self.activar_borrador,
        ).pack(side="left", padx=10, pady=4)

        # Lienzo donde se dibuja
        self.lienzo = tk.Canvas(ventana, width=700, height=500, bg=COLOR_FONDO)
        self.lienzo.pack()

        # Eventos del mouse
        self.lienzo.bind("<B1-Motion>", self.dibujar)        # mover con clic presionado
        self.lienzo.bind("<ButtonRelease-1>", self.soltar)   # soltar el clic

    def cambiar_color(self, color):
        self.color_actual = color
        self.grosor_actual = GROSOR_LAPIZ

    def activar_borrador(self):
        # El borrador pinta del mismo color del fondo y con trazo más grueso
        self.color_actual = COLOR_FONDO
        self.grosor_actual = GROSOR_BORRADOR

    def dibujar(self, evento):
        if self.ultimo_x is not None:
            self.lienzo.create_line(
                self.ultimo_x, self.ultimo_y, evento.x, evento.y,
                fill=self.color_actual, width=self.grosor_actual,
                capstyle="round", smooth=True,
            )
        self.ultimo_x = evento.x
        self.ultimo_y = evento.y

    def soltar(self, evento):
        self.ultimo_x = None
        self.ultimo_y = None


def main():
    ventana = tk.Tk()
    Paint(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
