from tkinter import *
from tkinter import ttk

#Ventana = Tk()
#cuadro = ttk.Frame(Ventana, padding = 10)
#cuadro.grid()
#ttk.Label(cuadro, text = "Otra ventana").grid(column=0, row=0)
#ttk.Button(cuadro, text="Salir", command=Ventana.destroy).grid(column =1, row=0)
#lbl= Label(Ventana, text="Una Ventana", font =("italic", 16))
#lbl.place(x=0, y=0)
#Ventana.title('Hola')
#Ventana.geometry("480x320")
#Ventana.mainloop()



# ventana de con entrada de Texto
V = Tk()
V.title("Texto de Envio")
V.geometry('480x320')
def printInput():
	inp = inputtxt.get(1.0, "end-1c")
	lbl.config(text = "Entrada: " + inp)
	print(inp)

inputtxt = Text(V, height = 1, width = 20)
inputtxt.pack()
printButton = Button(V,text = "Print", command = printInput)
printButton.pack()

lbl = Label(V, text = "")
lbl.pack()
V.mainloop()
