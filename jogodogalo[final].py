import tkinter as tk
import time
from threading import Timer

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

current_value = 1

def check_winner():
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
            return matrix[i][0]
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
            return matrix[0][i]
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
        return matrix[0][2]
    return None

def update_value(row, col):
    global current_value
    if matrix[row][col] == 0:
        matrix[row][col] = current_value
        buttons[row][col].config(text="X" if current_value == 1 else "O")
        winner = check_winner()
        if winner:
            display_winner("X" if winner == 1 else "O")
        else:
            current_value = 2 if current_value == 1 else 1

def display_winner(winner):
    label = tk.Label(root, text=f"{winner} wins!", font=("Arial", 16))
    label.grid(row=3, column=0, columnspan=3)
    Timer(5, root.destroy).start()

root = tk.Tk()
root.title("Matrix Grid")

buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="", width=5, height=2,
                           command=lambda r=row, c=col: update_value(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

root.mainloop()
