## PYTHON
from machine import Pin, ADC, PWM
from time import sleep

potenciometro = ADC(Pin(34))
led = PWM(Pin(21), freq=5000)

potenciometro.atten(ADC.ATTN_11DB)

while True:
    valor_potenciometro = potenciometro.read()
    valor_pwm = int(valor_potenciometro * 1023 / 4095)
    
    led.duty(valor_pwm)
    
    print("ADC:", valor_potenciometro, "| PWM:", valor_pwm)
    
    sleep(0.1)


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
