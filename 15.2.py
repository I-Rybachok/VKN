#Розробити  екранний  додаток,  який  здійснюватиме  шифрування  і дешифрування повідомлень шифром Цезаря.
import tkinter as tk
from math import *


def act():
    e1 = e.get()
    list = [] 
    for i in e1:
        list.append(i)
    print(list)
    if i == 'a':
        n = 0
        e.delete(n, tk.END)
        e.insert(0, 'd')
        
    if i == 'b':
        n = n+1
        e.delete(n, tk.END)
        e.insert(0, 'e')
       
    if i == 'c':
        e.delete(0, tk.END)
        e.insert(0, 'f')
    if i == 'd':
        e.delete(0, tk.END)
        e.insert(0, 'g')
    if i == 'e':
        e.delete(0, tk.END)
        e.insert(0, 'h')
    if i == 'f':
        e.delete(0, tk.END)
        e.insert(0, 'i')
    if i == 'g':
        e.delete(0, tk.END)
        e.insert(0, 'j')
    if i == 'h':
        e.delete(0, tk.END)
        e.insert(0, 'k')
    if i == 'i':
        e.delete(0, tk.END)
        e.insert(0, 'l')
    if i == 'j':
        e.delete(0, tk.END)
        e.insert(0, 'm')
    if i == 'k':
        e.delete(0, tk.END)
        e.insert(0, 'n')
    if i == 'l':
        e.delete(0, tk.END)
        e.insert(0, 'o')
    if i == 'm':
        e.delete(0, tk.END)
        e.insert(0, 'p')
    if i == 'n':
        e.delete(0, tk.END)
        e.insert(0, 'q')
    if i == 'o':
        e.delete(0, tk.END)
        e.insert(0, 'r')
    if i == 'p':
        e.delete(0, tk.END)
        e.insert(0, 's')
    if i == 'q':
        e.delete(0, tk.END)
        e.insert(0, 't')
    if i == 'r':
        e.delete(0, tk.END)
        e.insert(0, 'u')
    if i == 's':
        e.delete(0, tk.END)
        e.insert(0, 'v')
    if i == 't':
        e.delete(0, tk.END)
        e.insert(0, 'w')
    if i == 'u':
        e.delete(0, tk.END)
        e.insert(0, 'x')
    if i == 'v':
        e.delete(0, tk.END)
        e.insert(0, 'y')
    if i == 'w':
        e.delete(0, tk.END)
        e.insert(0, 'z')
    if i == 'x':
        e.delete(0, tk.END)
        e.insert(0, 'a')
    if i == 'y':
        e.delete(0, tk.END)
        e.insert(0, 'b')
    if i == 'z':
        e.delete(0, tk.END)
        e.insert(0, 'c')
    

win=tk.Tk()
win.title('Шифр Цезаря')

f = tk.Frame(background='grey', width=400, height=300)
f.pack()

l = tk.Label(master = f, text = 'Введіть текст та натисніть "Готово"', foreground="black", background='grey', width=100, height=5)
l.pack()

e = tk.Entry(master = f, foreground = 'black', background = 'white', width = 100)
e.pack(fill = tk.X)

b = tk.Button(master = f, text="Готово", width=25, height=5, background="red", foreground="white", command = act)
b.pack()

win.mainloop()