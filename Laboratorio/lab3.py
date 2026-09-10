int potenciometro = 18;
int led = 21;

int valorpotenciometro = 0;
int valorpwm = 0;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
}

void loop() {
  valorpotenciometro = analogRead(potenciometro);

  valorpwm = map(valorpotenciometro, 0, 4095, 0, 255);

  analogWrite(led, valorpwm);

  Serial.print("Potenciometro: ");
  Serial.print(valorpotenciometro);
  Serial.print("; brillo led: ");
  Serial.println(valorpwm);

  delay(10);
}
