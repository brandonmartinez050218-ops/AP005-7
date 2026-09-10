int potenciometro = D18;
int led = D21;

int valorpotenciometro = 0;
int valorpwm = 0;

void setup(){
  Serial.begin(115200);
  pinMode(led, OUTPUT);

}
void loop(){
  valorpotenciometro = analogRead(potenciometro);

  valorpwm = map(valorpotenciometro,0,4095,0,255);

  analogWrite(led,valorpwm);

  Serialprint("Potenciometro: ");
  Serialprint(valorpotenciometro);
  Serialprint("; brillo led: ");
  Serialprint(valorpwm);
  delay(10);
}
