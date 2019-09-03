from machine import Pin
from time import sleep

led = Pin(23, Pin.OUT)

sw = Pin(22, Pin.IN)
light = False
last_lighter = False
counter = 0


while True:
    print("Switch value = ", sw.value())

    if sw.value() == 0:
        if light:
            if last_lighter:
                pass        
            else:        
                light = False

        elif light == False:
            if last_lighter == False:
                light = True
            else:
                light = False
        last_lighter = True
    else:
        last_lighter = False

    if light :
        led.value(1)
    else:
        led.value(0)
     

    # sleep(0.3)