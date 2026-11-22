# -*- coding: utf-8 -*-
import tkinter as tk
from paint import Paint  # Tu archivo original sin tocar


def hacer_mas_bonito(app):
    app.ventana.configure(bg="#F1F5F9", padx=10, pady=10)
    app.lienzo.configure(highlightthickness=1, highlightbackground="#CBD5E1")

    for widget in app.ventana.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.configure(bg="#F1F5F9")
            for hijo in widget.winfo_children():
                if isinstance(hijo, tk.Label):
                    hijo.configure(bg="#F1F5F9", font=("Segoe UI", 10, "bold"))
                elif isinstance(hijo, tk.Button):
                    hijo.configure(relief="flat", bd=1, cursor="hand2")
                    if hijo.cget("bg") == "orange":
                        hijo.configure(fg="black")


def main():
    ventana = tk.Tk()
    app = Paint(ventana)
    hacer_mas_bonito(app)
    ventana.mainloop()


if __name__ == "__main__":
    main()
