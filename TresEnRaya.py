import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")

        # Variables del juego
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones = []

        # Crear botones de la cuadrícula
        for i in range(9):
            btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.marcar_casilla(i))
            btn.grid(row=i // 3, column=i % 3)
            self.botones.append(btn)

        # Botón para reiniciar el juego
        self.btn_reset = tk.Button(root, text="Reiniciar", font=("Arial", 14),
                                   command=self.reiniciar_juego)
        self.btn_reset.grid(row=3, column=0, columnspan=3, pady=10)

    def marcar_casilla(self, i):
        if self.tablero[i] == "" and not self.verificar_ganador():
            self.tablero[i] = self.turno
            self.botones[i].config(text=self.turno)

            # Verificar si hay un ganador
            if self.verificar_ganador():
                messagebox.showinfo("¡Fin del Juego!", f"¡{self.turno} ha ganado!")
                return
            elif "" not in self.tablero:  # Verificar empate
                messagebox.showinfo("¡Fin del Juego!", "¡Empate!")
                return

            # Cambiar turno
            self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)             # Diagonales
        ]

        for a, b, c in combinaciones:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] and self.tablero[a] != "":
                return True
        return False

    def reiniciar_juego(self):
        self.turno = "X"
        self.tablero = [""] * 9
        for btn in self.botones:
            btn.config(text="")

# Ejecutar la aplicación
root = tk.Tk()
app = TicTacToe(root)
root.mainloop()
