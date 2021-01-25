#Import libraries

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print('Coordinate Program Has Started!')
print('HOLD IN "n" IF YOU WANT TO STOP THE SCRIPT WHILE ITS RUNNING')
option1=input('[1] to run, [2] to set up (first time), [0] to exit: ')

a=True
while a==True:
    if (option1=='1' or option1=='[1]' or option1=='2' or option1=='[2]' or option1=='0' or option1=='[0]'):
        a=False
    else:
        print('?, You have to write 1, 2 or 0')
        option1=input('[1] to run, [2] to set up (first time), [0] to exit: ')


if option1==('2' or '[2]'):
    print('The setup has started.')
    print('You have to find 5 coordinates on your krita client.')
    print('Put your cursor in the middle of the krita canvas.')
    x1=input('What was the X-coordinate: ')
    y1=input('What was the Y-coordinate: ')
    print('Click on the "transform a layer or a selection".')
    print('Click on "Tools Options" and pull down the menu such that the X and Y position is always visable.')
    print('Put your cursor on the "+1" button but the X-position.')
    x2=input('What was the X-coordinate: ')
    y2=input('What was the Y-coordinate: ')
    print('Put your cursor on the "-1" button but the X-position.')
    x3=input('What was the X-coordinate: ')
    y3=input('What was the Y-coordinate: ')
    print('Put your cursor on the "+1" button but the Y-position.')
    x4=input('What was the X-coordinate: ')
    y4=input('What was the Y-coordinate: ')
    print('Put your cursor on the "-1" button but the Y-position.')
    x5=input('What was the X-coordinate: ')
    y5=input('What was the Y-coordinate: ')
    with open('data.txt', 'w') as f:
        f.write(' '+x1+' '+y1+' '+x2+' '+y2+' '+x3+' '+y3+' '+x4+' '+y4+' '+x5+' '+y5+' ')
    f.close()
    option2=input('[1] to run, [0] to exit: ')
    a=True
    while a:
        if (option2=='1' or option2=='[1]' or option2=='0' or option2=='[0]'):
            a=False
        else:
            print('?, You have to write 1 or 0')
            option1=input('[1] to run, [0] to exit: ')
            if (option2=='0' or option2=='[0]'):
                exit()
        





print('Click on the object you want to move using the "transform a layer or selection tool".')
print('Open the "Tool Options" panel.')
x6=int(input('What is the X-coordinate: '))
y6=int(input('What is the Y-coordinate: '))

print('Move the object to the position you want the object to end up at.')
x7=int(input('What is the X-coordinate: '))
y7=int(input('What is the Y-coordinate: '))

z1=int(input('How many keyframes do you want for the animation (more=smoother): '))
z2=max(0.02, float(input('How many seconds per keyframe do you want (minimum 0.02, increase if u lag): ')))



#Insert Variables

startXY=[x6,y6] 
stopXY=[x7,y7] 
iteration=z1 
timeT=z2 

pyautogui.PAUSE = timeT

#Calculations

deltaX=(stopXY[0]-startXY[0])/iteration
deltaY=(stopXY[1]-startXY[1])/iteration




#Script


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
 


with open('data.txt', 'r') as u:
    data=u.read()
u.close()



r=True
w=True
h=0
g=0
j=0
while r:
    if data[h]==' ':
        while w:
            g+=1
            if data[h+g]==' ':
                w=False
                j+=1
                if j==1:
                    x1=int(data[h+1:(h+g)])
                elif j==2:
                    y1=int(data[h+1:(g+h)])
                elif j==3:
                    x2=int(data[h+1:(g+h)])
                elif j==4:
                    y2=int(data[h+1:(g+h)])
                elif j==5:
                    x3=int(data[h+1:(g+h)])
                elif j==6:
                    y3=int(data[h+1:(g+h)])
                elif j==7:
                    x4=int(data[h+1:(g+h)])
                elif j==8:
                    y4=int(data[h+1:(g+h)])
                elif j==9:
                    x5=int(data[h+1:(g+h)])
                elif j==10:
                    y5=int(data[h+1:(g+h)])
                    r=False
    h+=1
    g=0
    w=True
    

    


sum1DeltaX=0
sum2DeltaX=0
sum1DeltaY=0
sum2DeltaY=0




for x in range(iteration):
    sum1DeltaX+=deltaX
    difX=round(sum1DeltaX)-round(sum2DeltaX)
    sum2DeltaX+=deltaX
    click(x1, y1)
    for y in range(abs(difX)):
        if difX>0:
            click(x2, y2)  
        elif difX<0:
            click(x3, y3)
    sum1DeltaY+=deltaY
    difY=round(sum1DeltaY)-round(sum2DeltaY)
    sum2DeltaY+=deltaY
    for z in range(abs(difY)):
        if difY>0:
            click(x4, y4)
        elif difY<0:
            click(x5, y5)
    click(x1, y1)
    pyautogui.keyDown('right')
    if keyboard.is_pressed('n'):
        exit()


 
