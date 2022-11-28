from tkinter import *
import math

def korin():
    n1 = e.get()
    n = float(n1)
    a = math.sqrt(n)
    e.delete(0, END)
    e.insert(0,a)

win=Tk()
win.title('Калькулятор коренів')

f = Frame(background='green', width=400, height=300)
f.pack()

l = Label(master=f, text = 'Введіть число та натисніть "Готово"', foreground="white", background='green')
l.pack()

e = Entry(master=f,foreground="black", background='white', width=100)
e.pack()

b = Button(master=f, text="Готово", width=25, height=5, background="blue", foreground="yellow", command = korin)
b.pack()

win.mainloop()
