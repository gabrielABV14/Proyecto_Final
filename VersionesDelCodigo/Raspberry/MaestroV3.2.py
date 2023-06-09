from tkinter import * #Importamos todas las funciones de tkinter 
from smbus import SMBus #Importamos la libreria para la comunicacion i2c
import time #Importamos la libreria de tiempo para hacer pausas bloqueantes

#Configuramos la comunicacion I2C
direccion = 0x30 #definimos una direccion arbitraria para el esclavo
bus = SMBus(1) #Creamos un objeto de tipo SMBus (Por defecto es 1)
registro = 0x00 #Definimos un numero para el registro(En este caso no es importante)

bandera = 0 # definimos una bandera como variable global
bandera2 = 2 #Definimos una segunda Bandera

try: # inicio de una secuencia Try

	Ventana = Tk() # Declara un objeto de tipo ventana
	Ventana.title("MaestroV3") #Definimos el titulo de la ventana de la interfaz
	Ventana.geometry("480x320") #definimos el tamaño de la ventana(480x320)

	def imprimir(): #creamos la funcion para mostrar el dato
		numero = 890 #Definimos una variable con el codigo 
		if(numero < 0): #Preguntamos si el valor es negativo
			registro = 0x00 #definimos el valor de registro(Es arbitrario)
			numero_abs = numero*(-1) #sacamos el valor absoluto del valor negativo
			Valor_Bytes = [(numero_abs >> 8) & 0xFF, numero_abs & 0xFF] # Convertimos el numero en su forma de bytes
			bus.write_i2c_block_data(direccion, registro, Valor_Bytes) # Enviamos el valor por i2c al arduino
		else: #si se entro a esta seccion significa que el numero es negativo
			registro = 0x01 # Definimos el valor de registro(Es Arbitrario)
			Valor_Bytes = [(numero >> 8) & 0xFF, numero &0xFF] #Convertimos el valor a su forma de Bytes
			bus.write_i2c_block_data(direccion,registro,Valor_Bytes) # Enviamos el dato por i2c al arduino
			time.sleep(0.05) #Esperamos un breve periodo de tiempo
			num = bus.read_byte_data(direccion,0x00) #Leemos el dato que deberia haber enviado el Arduino
			num2 = str(num) #convertimos ese dato a una cadena de caracteres
			Et2_Dato1.config(text = num2) # Cambiamos ese valor en la etiqueta para poder mostrar el dato

	def activar(): # definimos una funcion para activar los botones
		global bandera #Definimos que estamos editando una varible global
		if(bandera == 0): #preguntamos el estado de la bandera(Si esta en cero)
			Valor_Bytes=[(bandera >> 8) & 0xFF, bandera & 0xFF] #Convertimos el valor a su forma de bytes
			bus.write_i2c_block_data(direccion, registro, Valor_Bytes) #Enviamos el valor por I2C
			Btn2_ONOFF.config(text="on") #Cambiamos el texto del boton
			Btn2_ONOFF.config(fg = "green") #Cambiamos el color del texto del boton
			bandera = 1 #Cambiamos el valor de la bandera
		elif(bandera == 1): #Si entro en esta linea significa que la bandera es uno
			Valor_Bytes=[(bandera >> 8) & 0xFF, bandera & 0xFF] #Canvertimos el valor a su forma de bytes
			bus.write_i2c_block_data(direccion, 0x01, Valor_Bytes) #Enviamos el valor por i2c
			Btn2_ONOFF.config(text="off") #Cambiamos el texto del Boton
			Btn2_ONOFF.config(fg = "red") #Cambiamos el color del texto del boton a rojo
			bandera = 0 #Cambiamos el valor de la bandera

	def activar2(): #Creamos una funcion para el segundo Boton
		global bandera2 # Llamamos a la bandera2 como variable global
		if(bandera2 == 2): #preguntamos el valor de la variable si es 2
			Valor_Bytes=[(bandera2 >> 8) & 0xFF, bandera2 & 0xFF] #Convertimos a su forma de Bytes
			bus.write_i2c_block_data(direccion, 0x01, Valor_Bytes) #Enviamos el dato convertido por i2c
			bandera2 = 3 #Cambiamos el valor de la Bandera
			Btn3_ONOFF.config(text="on") #Cambiamos el valor de texto del boton
			Btn3_ONOFF.config(fg = "green") #Cambiamos el color de texto del Boton
		elif(bandera2 == 3): #Preguntamos el valor de la variable
			Valor_Bytes=[(bandera2 >> 8) & 0xFF, bandera2 & 0xFF] #Convertimos el numero a su forma de Bytes
			bus.write_i2c_block_data(direccion, 0x01, Valor_Bytes) #Enviamos el valor por i2c 
			bandera2 = 2 # Actualizamos el valor de la bandera
			Btn3_ONOFF.config(text="off") # Cambiamos el texto del Boton
			Btn3_ONOFF.config(fg = "red") # Cambiamos el color del Texto del boton

	Base = Frame(Ventana,width=480, height = 320) # Creamos un contenedor para nuestros botones
	Base.place(x=0,y=0) #colocamos el contenedor
	Base.config(bg = "#1565C0") #Definimos el color de fondo
	Base.config(bd = 2) #Definimos el grosor del Borde
	#entradaTexto = Text(Base,height = 1, width = 10) (Esta linea esta comentada y solo es de referencia)
	#entradaTexto.place(x=0,y=0) (Esta linea esta comentada y solo es de referencia)
	Boton = Button(Base, text = "Mostrar datos", command=imprimir) # Creamos un objeto de tipo boton que ejecute la secuencia de imprimir(Revisar arriba)
	Boton.place(x=50,y=116) #Colocamos el boton en una posicion indicada por X y Y
	Et1_Nombre1 = Label(Base, text="H",height = 1, width=1,fg = "#b5b5b5", bg="#666666", font = ('Times',20)) # Creamos una etiqueta con el titulo
	Et1_Nombre1.place(x=50,y=50) #Colocamos la etiqueta
	Et2_Dato1 = Label(Base, text="Vacio",height=1, width=5, fg="#b5b5b5", bg="#515151", font=('Times',20)) #Creamos una etiqueta para recinir el dato del sensor
	Et2_Dato1.place(x=122,y=50) # Colocamos la etiqueta
	Et3_Nombre2 = Label(Base, text="Humo", height = 1, width=5, fg="#b5b5b5", bg = "#666666", font=('Times',20)) #Creamos una etiqueta para mostrar un nombre
	Et3_Nombre2.place(x=50,y=80) #Colocamos la etiqueta
	Et4_Dato2 = Label(Base,text="Vacio",height=1, width=5, fg="#b5b5b5", bg="#515151", font=('Times',20)) #Creamos una etiqueta para recibir el dato de un sensor
	Et4_Dato2.place(x=122,y=80) #COlocamnos esa etiqueta
	Btn2_ONOFF = Button(Base,text="on",command=activar, fg="green") #Creamos un objeto de tipo boton que ejecute la secuencia de "activar" (revisar arriba)
	Btn2_ONOFF.place(x=286,y=178) #Colocamos el boton
	Btn3_ONOFF = Button(Base,text="on",command=activar2, fg="green")
	Btn3_ONOFF.place(x=286,y=220) # Colocamos el boton en una posicion arbitraria



	lienzo = Canvas(Base,width=128, height=128) #Creamos un lienzo para colocar dibujos
	lienzo.place(x=286,y=50 ) #Colocamos el lienzo
	#lienzo.create_polygon(10,0,0,40,40,40,fill='green')
	im = PhotoImage(file='v.gif') # creamos un objeto de tipo imagen 
	lienzo.create_image(50,50,image=im) # COlocamos el objeto de tipo imagen en el canvas

	lienzo2 = Canvas(Base,width=100, height=60) #Creamos un lienzo para dibujar 
	lienzo2.place(x=50,y=150)  #Colocamos el lienzo en una ubicacion aleatoria
	photo = PhotoImage(file='al.png') #Creamos un Objeto de tipo imagen
	lienzo2.create_image(50,30,image=photo) # Colocamos la imagen en el lienzo





	Ventana.mainloop() #Secuencia de la ventana


except KeyboardInterrupt: #Secuencia de recepcion de error
	print("Se activo la interrupcion por teclado") # Esto es autodescriptivo
except ValueError as Error: # Secuencia de recepcion de error y renombramos la variable
	print("Lo sentimos ha ocurrido un error: ") # Esto es autodescriptivo
	print(Error) #Imprimimos el error
