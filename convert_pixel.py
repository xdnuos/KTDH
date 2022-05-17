from khaibao import *
def convert_coordinate_axis(x,y):
        modulo_x=x%UNIT
        modulo_y=y%UNIT
        x = (x - modulo_x - end_x/2+start_x)/UNIT
        y = (end_y/2 - (y-modulo_y)+start_y)/UNIT
        return int(x),int(y)

def revert_coordinate_axis(x,y):
        x = x*UNIT + int(grid_x/2)+20 # +20 là vì dịch lưới sang trái và xuống dưới 20px
        y = -y*UNIT + int(grid_y/2)+20
        return x,y