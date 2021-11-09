"""imports"""
from turtle import *#turtle draws the process.
from math import pi#we need pi to calculate the moves needed in 90 degrees. current number*pi/90=move (if we turn 1 degree right each time).

"""setup"""
x,y,first,second=1,1,Turtle(),Turtle()#we define that the first numbers of the series are 1 and 1, than make 2 turtles named first and second.
speed(100000000000**10000)#we set a high speed to reach maximum speed, since this code requires tons of calculations.
first.hideturtle()
second.hideturtle()
hideturtle()#we make the two invisible to see the spiral without them(we also hide the defualt one).
for z in range(1,10):#we dont like it running forever, so 10 times is enough to fill the screen. (5 is needed)
    
    """part one of process"""
    y=x+y#we set the new fibonacci value.
    for UselessVariable in range(0,90):#loop for 90-0 times (90).
        first.backward(x*pi/90)
        second.forward(x*pi/90)#we move the two forward and backward.
        first.left(1)
        second.right(1)#we rotate them
        
    """part two of process"""
    x=x+y#we set the new current fibonacci value.
    for UselessVariable in range(0,90):#we do it again, just with y, which is required for the fibonacci series (read about the other projects for this).        
        first.backward(y*pi/90)
        second.forward(y*pi/90)#we move them        
        first.left(1)
        second.right(1)#we rotate them
        
    """progress prints"""
    print(str(z*10)+'% done')#print percent of work done
print('done drawing')#print done drawing when its done
