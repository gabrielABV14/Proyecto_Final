from tkinter import *
from tkinter import ttk
from smbus import SMBus
import time

# Configurar I2C
D = 0x30 # Direccion del I2C (Arbitraria)
bus = SMBus(1) # definir el bus (Por defecto es 1)
registro =0x00 # Definimos el numero de registro (Es arbitrario)


#iniciamos secuencia eternaV1
try:

	V = Tk() #Una definicion de Tkinter
	V.title("VentanaMaestra") # Definimos ntitulo de la Ventana
	V.geometry('480x320') # Tamaño del Ventana

	def Imprimir(): # Funcion de impresion
		i = entradaTexto.get(1.0, "end-1c") # Obtenemos texto de l cuadro de texto
		et.config(text = "Dato: "+ i) # Configuramos una Etiqueta para Mostrar los datos enviados
		if(i == ""): # Revisamos si el dato esta vacio
			et.config(text = "Dato vacio")
		else: # si el dato no esta vacio entonces:
			numero = int(i) # transformamos a entero
			if(numero < 0): # Preguntamos si el numero es negativo
				registro = 0x00 # Definimos el registro
				numero_abs = numero*(-1) #definimos el registro para idenbtificar el numero como negativo
				Valor_bytes = [(numero_abs >> 8) & 0xFF, numero_abs &  0xFF] # Convertir valor en su variante de Bytes
				bus.write_i2c_block_data(D, registro, ValorBytes) # Enviar por i2c los datos
			elif(numero >= 0): # Si es positivo
				registro = 0x01 # definimos el valor del registro para decir que es positivo
				Valor_bytes = [(numero >> 8) & 0xFF, numero & 0xFF] # Cambiamos el valor a su variante en forma de bytes
				bus.write_i2c_block_data(D, registro, Valor_bytes) # Enviar datos por i2c
			if(numero == 890): # Preguntamos por un valor especifico
				time.sleep(0.05) # Definimos una pausa bloqueante (Arbitraria)
				num = bus.read_byte_data(D,0x00) # leemos los datos del cache del i2c
				print(num) # imprimimos el valor leido por consola
				num2 = str(num)
				et.config(text = "Dato del Sensor: "+ num2)

		print(i) # Imprimimos  por consola el dato, solo como Verificacion

	entradaTexto = Text(V,height = 1, width = 20) # creamos un cuadro de texto
	entradaTexto.pack() # empaquetamos el cuadro de texto
	Boton = Button(V, text = "Print", command = Imprimir) # Creamos un Boton
	Boton.pack() # empaquetamos el Boton

	et = Label(V, text = "Vacio") # Creamos una etiqueta cun el texto vacio
	et.pack() # empaquetamos la etiqueta
	V.mainloop() # inicamos un ciclo de ventana

except KeyboardInterrupt:
	print("Se activo la Interrupcion por Teclado") # Una Advertencia

except ValueError as Error:
	print("Lo Sentimos Ha ocurrido un Error: ") # Mensaje Generico
	print(Error) # Imprimir codigo del error
