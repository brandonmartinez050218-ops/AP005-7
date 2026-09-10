from machine import Pin, ADC
from time import sleep

led = Pin(2, Pin.OUT)
pot = ADC(Pin(34))

pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

while True:
    valor = pot.read()
    print(valor)

    if 1800 <= valor <= 2300:
        led.on()
    else:
        led.off()

    sleep(0.1)
