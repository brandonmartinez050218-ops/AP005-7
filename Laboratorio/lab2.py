## PYTHON
int led = 21;

void setup() {
  pinMode(led, OUTPUT);

  for (int i = 0; i < 5; i++) {
    digitalWrite(led, HIGH);
    delay(1000);

    digitalWrite(led, LOW);
    delay(1000);
  }
}
void loop() {
}




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
