from smbus import SMBus


#Configuraciones de I2C
address = 0x30 #DIreccion
bus = SMBus(1)
registro = 0x00

try:

	while True:
		comando = input("Ingresar Numero: \n") #recibe un dato por teclado

		numero = int(comando) #convertimos string a entero
		if(numero < 0): #Pregunta si el numero es negativo
			registro = 0x00 #definimos registro
			numero_abs = numero*(-1) #Sacamos Valor Absoluto
			Valor_bytes = [(numero_abs >> 8) & 0xFF, numero_abs & 0xFF] #convertimos el numero en Bytes
			bus.write_i2c_block_data(address,registro,Valor_bytes) #escribimos en el i2c

		elif(numero >= 0): #si es positivo
			registro = 0x01 #Cambiamos el valor de registro
			Valor_bytes = [(numero >> 8) & 0xFF,numero & 0xFF] #Cambia el numero en su forma de Bytes
			bus.write_i2c_block_data(address,registro,Valor_bytes) #envia los bytes por i2c
except KeyboardInterrupt:

	print("Interrupcion por Teclado") #excepcion de teclado
except ValueError as ve:
	print(ve)
	print("Otro Error") #imprimimos error
