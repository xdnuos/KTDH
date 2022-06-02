from graphics import *
from time import sleep
import button as BT
import easygui

max_x=500
max_y=500
_UNIT = 5
_COLOR="red"

win = GraphWin('BT 1', max_x+100, max_y)#tạo 1 cửa sổ 500px x 500px

def draw_grid(max_x,max_y):
    #vẽ đƯờng ngang
    for x in range(0,max_x,_UNIT):
        line = Line(Point( x + _UNIT,0), Point(x + _UNIT,max_y))
        line.setFill("gray")
        line.draw(win)

    #vẽ đường dọc
    for y in range(0,max_y,_UNIT):
        line = Line(Point( 0,y + _UNIT), Point(max_x,y + _UNIT))
        line.setFill("gray")
        line.draw(win)

    #vẽ trục toạ độ (làm đậm lên thôi :v)
    for x in range(int(max_x/2)-1,int(max_x/2)+1,1): #vẽ trục x
        line = Line(Point( x,0), Point(x,max_y))
        line.setFill("black")
        line.draw(win)
    for x in range(int(max_x/2+_UNIT)-1,int(max_x/2+_UNIT)+1,1): #vẽ trục x
        line = Line(Point( x,0), Point(x,max_y))
        line.setFill("black")
        line.draw(win)
    for y in range(int(max_y/2)-1,int(max_y/2)+1,1): #vẽ trục y
        line = Line(Point( 0,y), Point(max_x,y))
        line.setFill("black")
        line.draw(win)
    for y in range(int(max_y/2+_UNIT)-1,int(max_y/2+_UNIT)+1,1): #vẽ trục y
        line = Line(Point( 0,y), Point(max_x,y))
        line.setFill("black")
        line.draw(win)

def put_pixel(x,y,color):
    # if(x%_UNIT == 0 & y%_UNIT==0):
    #     for i in range(_UNIT+1):
    #         for j in range(_UNIT+1):
    #             win.plotPixel(x+i,y+j,color)
    # elif(x%_UNIT==0):
    #     modulo_y=y%_UNIT
    #     for i in range(_UNIT+1):
    #         for j in range(_UNIT+1):
    #             win.plotPixel(x+i,y-modulo_y+j,color)
    # elif(y%_UNIT==0):
    #     modulo_x=x%_UNIT
    #     for i in range(_UNIT+1):
    #         for j in range(_UNIT+1):
    #             win.plotPixel(x+i-modulo_x,y+j,color)
    # else:
    if(x<max_x):
        modulo_x=x%_UNIT
        modulo_y=y%_UNIT
        for i in range(_UNIT+1):
            for j in range(_UNIT+1):
                win.plotPixel(x+i-modulo_x,y+j-modulo_y,color)

# def draw_input_box(x,y,width):
#     inputBox = Entry(Point(x,y), width)
#     inputBox.draw(win)
def draw_text(x,y,string):
    txt=Text(Point(x,y),string)
    txt.draw(win)
def convert_coordinate_axis(x,y):
    modulo_x=x%_UNIT
    modulo_y=y%_UNIT
    x = (x - modulo_x - max_x/2)/_UNIT
    y = (max_y/2 - (y-modulo_y))/_UNIT
    return int(x),int(y)

def revert_coordinate_axis(x,y):
    x = x*_UNIT + 250
    y = -y*_UNIT + 250
    return x,y

draw_grid(max_x,max_y)  
bt_putpixel = BT.Button(win, Point(550,100), 80, 50, 'Put Pixel')

inputBox_X = Entry(Point(560,15), 5)
inputBox_X.draw(win)
draw_text(520,15,"X")

inputBox_Y = Entry(Point(560,50), 5)
inputBox_Y.draw(win)
draw_text(520,50,"Y")
while(1):
    p=win.getMouse() # pause for click in window
    put_pixel(int(p.x),int(p.y),_COLOR)
    if(p.x<501):
        new_x,new_y = convert_coordinate_axis(p.x,p.y)
        inputBox_X.setText(new_x)
        inputBox_Y.setText(new_y)
    if(bt_putpixel.clicked(p)):
        x = inputBox_X.getText()
        y= inputBox_Y.getText()
        try:
            new_x, new_y = revert_coordinate_axis(int(float(x)),int(float(y)))
            put_pixel(new_x,new_y,_COLOR)
        except ValueError:
            easygui.msgbox("X and Y not be empty", title="ERROR")
win.close()
