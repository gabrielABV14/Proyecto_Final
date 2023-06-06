from tkinter import *


V = Tk()

V.geometry("700x350")
cuadro = Frame()
cuadro.pack(side = "left")
cuadro.config(bg = "#ff80cd")
cuadro.config(bd=24)
cuadro.config(relief = "sunken")
cuadro.config(cursor="heart")
canvas = Canvas(cuadro, width=300, height=250) #.grid(column=0, row=0)
canvas.create_line(50,50,100,100, fill="red",width=10)
canvas.grid(column=0, row=0)

V.mainloop()
