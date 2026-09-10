## PYTHON
from machine import Pin
from time import sleep

led = Pin(21, Pin.OUT)

for i in range(5):
    led.on()
    sleep(1)

    led.off()
    sleep(1)


## C++
#include <Arduino.h>

int led = 21;

void setup() {
    pinMode(led, OUTPUT);

    for (int i (); i < 5; i++) {
        digitalWrite(led, HIGH);
        delay(1000);

        digitalWrite(led, LOW);
        delay(1000);
    }
}

void loop() {
}
