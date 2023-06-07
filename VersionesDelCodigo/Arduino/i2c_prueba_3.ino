// incluir libreria
#include <Wire.h>
// definir valores 
int p = 0; // sino
int q = 0; // valor1 
int r = 0; // valor2
int d = 0;
void setup() {
// configurar direcion i2c
Wire.begin(0x30); 
  // declarar evento de recibir 
  Wire.onReceive(receiveEvent);
  Wire.onRequest(Evento);
  Serial.begin(9600);
  pinMode(4,OUTPUT);
  digitalWrite(4,LOW);
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
    if(dato == 1)
    {
      digitalWrite(4,HIGH);
    }
    if(dato == 0)
    {
      digitalWrite(4,LOW);
    }
    if(dato == 890)
    {
      Serial.print("Se envio la orden al sensor:  ");
      d = analogRead(A0);
      Serial.println(d);
      
    }
    Serial.println(dato);
    Evento();
  }
}
void loop() {
  //delay(10);
  // no viene nada temporalmente 
}

void Evento()
{
  Wire.write(d);
}
