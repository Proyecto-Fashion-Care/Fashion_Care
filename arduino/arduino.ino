const int numLEDs = 3; //Numero de leds que vamos a poner
const int ledPins[numLEDs] = {32, 40, 48};
int option;

void setup() {
  Serial.begin(9600); //Inicializamos el puerto Serial
  //Configuramos los leds como salida
  for (int i=0; i<numLEDs; i++){
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  //Si escribimos algo en el puerto serial, Serial.available > 0
  if (Serial.available() >= 1){ 
    option = Serial.read(); //Leemos lo que hay en el puerto serial
    if (option == '1'){
      digitalWrite(ledPins[0], HIGH);
      digitalWrite(ledPins[1], LOW);      
      digitalWrite(ledPins[2], LOW);
    }
    if (option == '2'){
      digitalWrite(ledPins[0], LOW);
      digitalWrite(ledPins[1], HIGH);      
      digitalWrite(ledPins[2], LOW);
    }
    if (option == '4'){
      digitalWrite(ledPins[0], LOW);
      digitalWrite(ledPins[1], LOW);      
      digitalWrite(ledPins[2], HIGH);
    }
  }
}