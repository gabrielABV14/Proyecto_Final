// incluir libreria
#include <Wire.h>
// definir valores 
int p = 0; // sino
int q = 0; // valor1 
int r = 0; // valor2

void setup() {
// configurar direcion i2c
Wire.begin(0x30); 
  // declarar evento de recibir 
  Wire.onReceive(receiveEvent);

  

  Serial.begin(9600);
}
 // definimos funcion de recibimiento
void receiveEvent(int howMany) {
  while (Wire.available()) { 
     // tomamos el registro de dato de i2c
     p = Wire.read(); 
     // tomamos el primer dato de i2c
     q = Wire.read();
     // tomamos el segundo dato de i2c
     r = Wire.read();
    // devolvemos el valor de su formato de bytes a entero 
    int dato = (q*256)+r;
    if(p == 0){
      dato = dato*(-1);
    }
    Serial.println(dato);
    
  }
}
void loop() {
  //delay(10);
  // no viene nada temporalmente 
}
