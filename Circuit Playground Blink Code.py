import time
import board
from adafruit_circuitplayground import cp
x=0
y=0
z=0
t=0
e=0.005
a=1
while True:
    cp.pixels.fill((0,0,0))
    time.sleep(1)
    while x<255:
        time.sleep(t)
        for i in range(10):
            cp.pixels[i]=(x,y,z)
            x+=a
            time.sleep(e)
    while y<255:
        time.sleep(t)
        for i in range(10):
            cp.pixels[i]=(x,y,z)
            y+=a
            time.sleep(e)
    while z<255:
        time.sleep(t)
        for i in range(10):
            cp.pixels[i]=(x,y,z)
            z+=a
            time.sleep(e)
    while x>0:
        time.sleep(t)
        for i in range(10):
            cp.pixels[i]=(x,y,z)
            x-=a
            time.sleep(e)
    while y>0:
        time.sleep(t)
        for i in range(10):
            cp.pixels[i]=(x,y,z)
            y-=a
            time.sleep(e)
    while z>0:
        time.sleep(t)
        for i in range(10):
            cp.pixels[i]=(x,y,z)
            z-=a
            time.sleep(e)

