import tkinter as tk
import random

root = tk.Tk()
root.geometry('500x500')

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_oval(2, 2, 300, 300)
canvas.create_rectangle(2, 2,300, 300)

r = 150
trial = 10000
cnt = 0
i = 0

def result(a, b):
    label = tk.Label(root, text=f"{a / b * 4}")
    label.pack()
    

def point():
    global cnt, trial, i

    i += 1
    
    x = random.uniform(0, 300)
    y = random.uniform(0, 300)

    canvas.create_oval(x, y, x, y)

    if (x - 150)**2+(y - 150)**2 <= r**2:
        cnt += 1

    if i < trial:
        root.after(1, point)
    else:
        result(cnt, trial)

root.after(1, point)

root.mainloop()
