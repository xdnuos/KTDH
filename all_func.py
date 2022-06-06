from matplotlib.pyplot import axis
import pygame
from khaibao import *
import pygame_gui
import math
import numpy as np
_UNIT=5
white_color = (255,255,255)
class Put_pixel:
    def __init__(self,surface,arr):
        for element in arr:
            pygame.draw.rect(surface, element[2], pygame.Rect(element[0], element[1], _UNIT, _UNIT))
    def de_put(surface,arr):
        for element in arr:
            pygame.draw.rect(surface, white_color, pygame.Rect(element[0], element[1], _UNIT, _UNIT))
class Convert_coordinate:
    def mon2real(x,y):
        modulo_x=x%UNIT
        modulo_y=y%UNIT
        x = (x - modulo_x - end_x/2+start_x)/UNIT
        y = (end_y/2 - (y-modulo_y)+start_y)/UNIT
        return int(x),int(y)
    def real2mon(x,y):
        x = x*UNIT + int(grid_x/2)+20 # +20 là vì dịch lưới sang trái và xuống dưới 20px
        y = -y*UNIT + int(grid_y/2)+20
        return x,y
    def mon2real_arr(arr):
        for element in arr:
            modulo_x=(element[0]+2)%UNIT
            modulo_y=(element[1]+2)%UNIT
            element[0] = (element[0] - modulo_x - end_x/2+start_x)/UNIT
            element[1] = (end_y/2 - (element[1]-modulo_y)+start_y)/UNIT
        return arr
    def real2mon_arr(arr):
        for element in arr:
            #(-98,10) -> (535,260)
            element[0] = element[0]*UNIT + int(grid_x/2)+20-2 # +20 là vì dịch lưới sang trái và xuống dưới 20px
            element[1] = -element[1]*UNIT + int(grid_y/2)+20-2
        return arr
    def round(surface,arr):
        for element in arr:
            modulo_x=(element[0]+2)%_UNIT#243 % 5 = 3
            modulo_y=(element[1]+2)%_UNIT#152 % 5 = 2
            element[0]=element[0]-modulo_x
            element[1]=element[1]-modulo_y
        return arr
class Limit: #loại bỏ các giá trị vượt ra khỏi ô hiển thị -> tăng tốc xử lý
    def x(x):#dữ liệu vào là toạ độ thực tế
        if x < -round(grid_x/5/2):
            return -round(grid_x/5/2)
        if x > round(grid_x/5/2):
            return round(grid_x/5/2)
        return x
    def y(y):#dữ liệu vào là toạ độ thực tế
        if y < -round(grid_y/5/2):
            return -round(grid_y/5/2)
        if y > round(grid_y/5/2):
            return round(grid_y/5/2)
        return y
    def remove_px(arr): # dữ liệu vào là toạ độ màn hình
        new_arr=[]
        for x in arr:
            if not(x[0] < start_x-2 or x[0] > end_x+2 or x[1] < start_y-2 or x[1] > end_y+2):
                new_arr.append(x)
        new_arr=np.array(new_arr,dtype=object)
        return new_arr
class Draw_grid:
    def __init__(self,surface,manager,start_x,end_x,start_y,end_y):
        #vẽ đƯờng ngang
        for x in range(start_x,end_x+UNIT,UNIT):
            pygame.draw.line(surface,gray_color,(x,start_x),(x,end_y))
        #vẽ đường dọc
        for y in range(start_y,end_y+UNIT,UNIT):
            pygame.draw.line(surface,gray_color,(start_y,y),(end_x,y))
        #vẽ trục toạ độ
        pygame.draw.line(surface,black_color,(start_x,(end_y+start_y)/2),(end_x,(end_y+start_y)/2)) #trục y
        pygame.draw.line(surface,black_color,((end_x+start_x)/2,start_y),((end_x+start_x)/2,end_y)) #trục x
        #vẽ chữ cho 2 trục
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(500,0,40,20),
                                text="Y",
                                manager=manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(990,300,40,20),
                            text="X",
                            manager=manager)
class Draw():
    def rect(surface,x1,y1,x2,y2,color):#vẽ hình chữ nhật
        x1 = Limit.x(x1)
        x2 = Limit.x(x2)
        y1 = Limit.y(y1)
        y2 = Limit.y(y2)
        #(-10,-10,10,10)
        x_max=x1 #-10
        y_max=y1 #-10
        x_min=x2 #10
        y_min=y2 #10
        if(x2>x1):
            x_max=x2 #-> xmax = 10
            x_min=x1 #-> xmin =-10
        if(y2>y1):
            y_max=y2
            y_min=y1
        put_arr =[]
        for x in range(x_min,x_max+1): #20
            for y in range(y_min,y_max+1): #20
                # Put_pixel.revert(surface,x,y,red_color)
                put_arr.append([x,y,color]) #(0,0,red)?
        put_arr = np.array(put_arr,dtype=object)
        put_arr = Convert_coordinate.real2mon_arr(put_arr)
        Put_pixel(surface,put_arr)
    def PutPX(surface,arr,type):
        count =0
        new_arr=[]
        match type:
            case 1:
                for x in arr:
                    count+=1
                    if(count%3!=0):
                        new_arr.append(x)
                new_arr=np.array(new_arr,dtype=object)
                new_arr=Convert_coordinate.real2mon_arr(new_arr)
                Put_pixel(surface,new_arr)
            case 2:
                global dash_dot
                for x in arr:
                    count+=1
                    if(count%5!=0 and count!= dash_dot):
                        new_arr.append(x)
                    if(count==dash_dot):
                        dash_dot +=5
                new_arr=Convert_coordinate.real2mon_arr(new_arr)
                Put_pixel(surface,new_arr)
            case 3:
                global dash_dash_dot
                for x in arr:
                    count+=1
                    if(count%7!=0 and count!= dash_dash_dot):
                        new_arr.append(x)
                    if(count==dash_dash_dot):
                        dash_dash_dot+=7
                new_arr=Convert_coordinate.real2mon_arr(new_arr)
                Put_pixel(surface,new_arr)
            case default:
                new_arr=Convert_coordinate.real2mon_arr(arr)
                Put_pixel(surface,new_arr)
    def arrow(surface,x1,y1,x2,y2,color):
            x1 = Limit.x(x1)
            x2 = Limit.x(x2)
            y1 = Limit.y(y1)
            y2 = Limit.y(y2)
            Dx = (x2 - x1)
            Dy = (y2 - y1)
            arrowLength = round(math.sqrt(Dx ** 2 + Dy ** 2) / 6)
            if (arrowLength < 3):
                arrowLength = 3
            angle = math.atan2(Dy, Dx)
            x1_new = round(x2 - arrowLength * math.cos(angle - math.pi / 6))
            y1_new = round(y2 - arrowLength * math.sin(angle - math.pi / 6))
            x2_new = round(x2 - arrowLength * math.cos(angle + math.pi / 6))
            y2_new = round(y2 - arrowLength * math.sin(angle + math.pi / 6))
            Draw.line(surface,x2, y2, x1_new, y1_new,color)
            Draw.line(surface,x2, y2, x2_new, y2_new,color)
    def line(surface,x1,y1,x2,y2,color,type=0):
        x1 = Limit.x(x1)
        x2 = Limit.x(x2)
        y1 = Limit.y(y1)
        y2 = Limit.y(y2)
        ############## Sử dụng để vẽ nét đứt ###############
        #khai báo biến toàn cục
        global dash_dot
        global dash_dash_dot
        # count=1
        ############## END #################################
        ############## Thuật toán vẽ đường thẳng khi các đường thẳng đứng hoặc nằm ngang ############
        x = x1
        y = y1
        arr=np.array([[x,y,color]],dtype=object) # KHAI BÁO MẢNG
        # Put_pixel.revert(surface,x,y,red_color)# vẽ điểm đầu tiên
        arr = Convert_coordinate.real2mon_arr(arr)
        Put_pixel(surface,arr)
        xUNIT = 1
        yUNIT = 1; 
        #xét trường hợp để cho yUNIT và xUNIT để vẽ tăng lên hay giảm xuống
        if (x2 - x1 < 0):
            xUNIT = -xUNIT
        if (y2 - y1 < 0):
            yUNIT = -yUNIT
        if (x1 == x2):   # trường hợp vẽ đường thẳng đứng
            while (y != y2):
                y += yUNIT
                # count+=1
                # Draw.PutPX(surface,count,x,y,type)
                arr = np.append(arr,[[x,y,color]],axis=0)
        elif (y1 == y2):  #trường hợp vẽ đường ngang
            while (x != x2):
                x += xUNIT
                # count+=1
                # Draw.PutPX(surface,count,x,y,type)
                arr = np.append(arr,[[x,y,color]],axis=0)
        ##################### END #############################################
        else:          # trường hợp vẽ các đường xiên -> sử dụng thuật toán bresenham
        #########Thuật toán Bresenham vẽ đường thẳng##############
        # Trường hợp hệ số góc 0 < m <= 1:
        # P = 2dy – dx
        # nếu P >= 0 y++; P = P + (2dy – 2dx);
        # còn lại P = P + 2dy;

        # Trường hợp hệ số góc -1<= m < 0:
        # P = 2dy + dx
        # nếu P < 0 thì y–; P = P + (2dy + 2dx);
        # còn lại P = P + 2dy;

        # Trường hợp hệ số góc m > 1:
        # P = 2dx – dy
        # nếu P >=0 thì x++; P = P + (2dx – 2dy);
        # còn lại P = P + 2dx;

        # Trường hợp hệ số góc nhỏ m > -1:
        # P = 2dx + dy
        # nếu P < 0 thì x–; P = P+ (2dx + 2dy);
        # còn lại P = P + 2dx;

        #vì sử dụng trị tuyệt đối cho Dx và Dy nên loại bỏ 2 trường hợp m>-1 và -1<= m < 0
        #############################################
            Dx = abs(x2 - x1)
            Dy = abs(y2 - y1)
            m=Dy/Dx # trường hợp Dx = 0 đã được vẽ (đường thẳng đứng) 
            if(m>1):
                p=2*Dx-Dy
                while(x != x2):
                    if (p<0) :
                        p += 2*Dx
                    else:
                        p += 2*(Dx-Dy)
                        x += xUNIT
                    y += yUNIT
                    # count+=1
                    # Draw.PutPX(surface,count,x,y,type)
                    arr = np.append(arr,[[x,y,color]],axis=0)

            else:
                p = 2*Dy - Dx
                while(x != x2):
                    if (p<0) :
                        p += 2*Dy
                    else:
                        p += 2*(Dy-Dx)
                        y += yUNIT
                    x += xUNIT
                    # count+=1
                    # Draw.PutPX(surface,count,x,y,type)
                    arr = np.append(arr,[[x,y,color]],axis=0)
        Draw.PutPX(surface,arr,type)
        #trả lại giá trị ban đầu
        dash_dot=3
        dash_dash_dot=5
    def ve8diem(x0,y0,x,y,color,arr):
        arr.append([x0 + x , y0 + y,color])
        arr.append([x0 - x , y0 + y,color])
        arr.append([x0 + x , y0 - y,color])
        arr.append([x0 - x , y0 - y,color])
        arr.append([x0 + y , y0 + x,color])
        arr.append([x0 - y , y0 + x,color])
        arr.append([x0 + y , y0 - x,color])
        arr.append([x0 - y , y0 - x,color])
        return arr
    def circle(surface,x0,y0,r,color,type=0):
        x=0
        y=r
        p=3-2*r
        arr=[]
        while (x<=y):
            arr = Draw.ve8diem(x0,y0,x,y,color,arr)
            if(p<0):
                p=p+4*x+6
            else:
                p=p+4*(x-y)+10
                y=y-1
            x=x+1
        arr =np.array(arr,dtype=object)
        arr=Convert_coordinate.real2mon_arr(arr)
        Put_pixel(surface,arr)
    def ellipse(surface,x0,y0,r1,r2,color,type=0):
        count=0
        count1=0
        x=0
        y=r2
        c=r2/r1
        c=c*c
        p=2*c-2*r2+1
        arr=[]
        while (c*x<=y):
            if(type==1):
                if(count%3!=0):
                    # PX.Put_pixel.revert(surface,x0+x,y0+y,color)#1
                    # PX.Put_pixel.revert(surface,x0-x,y0+y,color)#2
                    arr.append([x0+x,y0+y,color])
                    arr.append([x0-x,y0+y,color])
                count+=1
            else:
                arr.append([x0+x,y0+y,color])
                arr.append([x0-x,y0+y,color])
            # PX.Put_pixel.revert(surface,x0+x,y0-y,color)#3
            # PX.Put_pixel.revert(surface,x0-x,y0-y,color)#4
            arr.append([x0+x,y0-y,color])
            arr.append([x0-x,y0-y,color])
            if (p<0):
                p += 2*c*(2*x+3)
            else:
                    p +=4*(1-y)+2*c*(2*x+3)
                    y-=1
            x+=1
        y=0;x=r1
        c= r1/r2
        c=c*c; p=2*c-2*r1+1
        while (c*y<=x):
            if(type==1):
                if(count1%3!=0):
                    # PX.Put_pixel.revert(surface,x0+x,y0+y,color)#1
                    # PX.Put_pixel.revert(surface,x0-x,y0+y,color)#2
                    arr.append([x0+x,y0+y,color])
                    arr.append([x0-x,y0+y,color])
                count1+=1
            else:
                arr.append([x0+x,y0+y,color])
                arr.append([x0-x,y0+y,color])
            arr.append([x0+x,y0-y,color])
            arr.append([x0-x,y0-y,color])
            if (p<0):
                p +=2*c*(2*y+3)
            else:
                    p +=4*(1-x)+2*c*(2*y+3)
                    x-=1
            y+=1
        arr = np.array(arr,dtype=object)
        Put_pixel(surface,Convert_coordinate.real2mon_arr(arr))