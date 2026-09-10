## PYTHON
int potenciometro = 34;
int led = 21;

int valorPotenciometro = 0;
int valorPWM = 0;
void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
}
void loop() {
 
  valorPotenciometro = analogRead(potenciometro);

  valorPWM = map(valorPotenciometro, 0, 4095, 0, 255);

  analogWrite(led, valorPWM);
  delay(100);
}

##c++

#include <Arduino.h>

int potenciometro = 34;
int led = 21;

int valorPotenciometro = 0;
int valorPWM = 0;

void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
  valorPotenciometro = analogRead(potenciometro);

  valorPWM = map(valorPotenciometro, 0, 4095, 0, 255);

  analogWrite(led, valorPWM);

  delay(100);
}
