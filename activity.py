
# import CPX library
from adafruit_circuitplayground import cp
from time import sleep

cp.pixels.brightness = 1
ndx = 9

while True:
    if cp.switch:
        if ndx > 9:
           ndx = 0
        else:
            cp.pixels[ndx] = (255,255,0)
            sleep(0.5)
            cp.pixels[ndx]  = (0,0,0)
            ndx +=1
    else:
        if ndx < 0:
           ndx = 9
        else:
            cp.pixels[ndx] = (255,255,255)
            sleep(0.5)
            cp.pixels[ndx] = (0,0,0)
            ndx -=1

