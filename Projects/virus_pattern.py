from time import sleep
from turtle import *
speed(0.3)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 2)
    b = b - 1
sleep(5)