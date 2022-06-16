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
            pygame.draw.rect(surface, element[2], pygame.Rect(element[0]-2, element[1]-2, _UNIT, _UNIT))
    def de_put(surface,arr):
        for element in arr:
            pygame.draw.rect(surface, white_color, pygame.Rect(element[0]-2, element[1]-2, _UNIT, _UNIT))
class Convert_coordinate:
    def mon2real(x,y):
        modulo_x=x%UNIT
        modulo_y=y%UNIT
        x = (x - modulo_x - int(grid_x/2)-start_x)/UNIT
        y = -(y - modulo_y - int(grid_y/2)-start_y)/UNIT
        return int(x),int(y)
    def real2mon(x,y):
        x = x*UNIT + int(grid_x/2)+20 # +20 là vì dịch lưới sang trái và xuống dưới 20px
        y = -y*UNIT + int(grid_y/2)+20
        return x,y
    def mon2real_arr(arr):
        for element in arr:
            modulo_x=element[0]%UNIT
            modulo_y=element[1]%UNIT
            element[0] = (element[0] - modulo_x - int(grid_x/2)-start_x)/UNIT
            element[1] = -(element[1] - modulo_y - int(grid_y/2)-start_y)/UNIT
        return arr
    def real2mon_arr(arr):
        for element in arr:
            #(-98,10) -> (535,260)
            element[0] = element[0]*UNIT + int(grid_x/2)+20 # +20 là vì dịch lưới sang trái và xuống dưới 20px
            element[1] = -element[1]*UNIT + int(grid_y/2)+20
        return arr
    def round(arr):
        for element in arr:
            modulo_x=(element[0])%_UNIT#243 % 5 = 3
            modulo_y=(element[1])%_UNIT#152 % 5 = 2
            if modulo_x >=2.5:
                element[0]=element[0]+5-modulo_x
            else:
                element[0]=element[0]-modulo_x
            if modulo_y >= 2.5:
                element[1]=element[1]+5-modulo_y
            else:
                element[1]=element[1]-modulo_y
        return arr
    def Chuyen_3Dto2D(x,y,z):
        # alpha = math.pi / 4
        # phi = math.pi / 4
        # L = z / math.tan(alpha)
        Xp = int(x - z * math.sqrt(2) / 2)
        Yp = int(y - z * math.sqrt(2) / 2)
        return Xp,Yp
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
    def xy(surface,manager,start_x,end_x,start_y,end_y):
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
    def xyz(surface,manager,start_x,end_x,start_y,end_y):
                #vẽ trục toạ độ
        pygame.draw.line(surface,black_color,((end_x+start_x)/2,(end_y+start_y)/2),(end_x,(end_y+start_y)/2)) #trục y
        pygame.draw.line(surface,black_color,((end_x+start_x)/2,start_y),((end_x+start_x)/2,(end_y+start_y)/2)) #trục x
        #vẽ chữ cho 2 trục
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(500,0,40,20),
                                text="Y",
                                manager=manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(990,300,40,20),
                            text="X",
                            manager=manager)
        pygame.draw.line(surface,black_color,(end_x/4-30,end_y),((end_x+start_x)/2,(end_y+start_y)/2)) #trục z
        #vẽ chữ cho 2 trục
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(20,600,40,20),
                                text="Z",
                                manager=manager)
class Draw():
    def rect(x1,y1,x2,y2,color,type=0):
        """type = 1 : vẽ nét đứt, mặc định là nét liền"""
        x1 = Limit.x(x1)
        x2 = Limit.x(x2)
        y1 = Limit.y(y1)
        y2 = Limit.y(y2)
        arr1 = Draw.line(x1,y1,x2,y1,color,type)
        arr2 = Draw.line(x1,y1,x1,y2,color,type)
        arr3 = Draw.line(x2,y1,x2,y2,color,type)
        arr4 = Draw.line(x1,y2,x2,y2,color,type)
        return np.concatenate((arr1,arr2,arr3,arr4))
    def rect_full(x1,y1,x2,y2,color):#vẽ hình chữ nhật
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
                put_arr.append([x,y,color]) #(0,0,red)?
        put_arr = np.array(put_arr,dtype=object)
        put_arr = Convert_coordinate.real2mon_arr(put_arr)
        return put_arr
    def PutPX(arr,type):
        """đã convert sang np và toạ độ màn hình"""
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
                return new_arr
            case 2:
                global dash_dot
                for x in arr:
                    count+=1
                    if(count%5!=0 and count!= dash_dot):
                        new_arr.append(x)
                    if(count==dash_dot):
                        dash_dot +=5
                new_arr=Convert_coordinate.real2mon_arr(new_arr)
                return new_arr
            case 3:
                global dash_dash_dot
                for x in arr:
                    count+=1
                    if(count%7!=0 and count!= dash_dash_dot):
                        new_arr.append(x)
                    if(count==dash_dash_dot):
                        dash_dash_dot+=7
                new_arr=Convert_coordinate.real2mon_arr(new_arr)
                return new_arr
            case default:
                new_arr=Convert_coordinate.real2mon_arr(arr)
                return new_arr
    def arrow(x1,y1,x2,y2,color):
            arr1 =[]
            arr2 =[]
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
            arr1 = Draw.line(x2, y2, x1_new, y1_new,color)
            arr2 = Draw.line(x2, y2, x2_new, y2_new,color)
            return np.concatenate((arr1,arr2))
    def line(x1,y1,x2,y2,color,type=0):
        """đã convert sang np và toạ độ màn hình\n
        type 1: - - | type 2:-.- | type 3:--.--"""
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
        # Put_pixel(surface,arr)
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
        #trả lại giá trị ban đầu
        dash_dot=3
        dash_dash_dot=5
        return Draw.PutPX(arr,type)
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
    def circle(x0,y0,r,color):
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
        return arr
    def ellipse(x0,y0,r1,r2,color,type=0):
        """
        Type = 0 là nét liền | Type =1 là nét đứt nửa trên, nét liền nửa dưới
        """
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
            else: #type = 0 -> ellipse binh thường
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
            else: #type = 0 -> ellipse binh thường
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
        return Convert_coordinate.real2mon_arr(arr)
    def flip_arr(arr):
        arr_len=len(arr) #4
        count=arr_len-1 #3
        for i in range(0,round(arr_len/2)): #4 lan
            tmp = arr[i,0] #6
            arr[i,0]= arr[count,0] # count =2 -> 9
            arr[count,0]=tmp
            # 1
            tmp = arr[i,1] #6
            arr[i,1]= arr[count,1] # count =2 -> 9
            arr[count,1]=tmp
            # 2
            tmp = arr[i,2] #6
            arr[i,2]= arr[count,2] # count =2 -> 9
            arr[count,2]=tmp
            count-=1
        return arr
    def remove_ellipse(arr,start,end):
        """ Hàm này để loại bỏ các điểm thừa để vẽ cung cho eclipse"""
        new_arr=[]
        if (start > 360 or end >360):
            start %= 360; end %= 360
        if (start > end):
            tmp = start
            start = end
            end = tmp
        for x in arr:
            if (x[3] >= start and x[3]<= end):
                new_arr.append(x)
        new_arr = np.array(new_arr,dtype=object)
        new_arr1 = np.zeros((int(new_arr.size/4),3),dtype=object)
        for x in range(int(new_arr.size/4)):
            new_arr1[x,0]=new_arr[x,0]
            new_arr1[x,1]=new_arr[x,1]
            new_arr1[x,2]=new_arr[x,2]
        return new_arr1
    def ellipse_2(r1,r2,color,start,end):
        """
        Vẽ ellipse với điểm đầu và điểm cuối do người dùng nhập vào\n
        r1,r2,color,start,end
        """
        x=0
        y=r2
        c=r2/r1
        c=c*c
        p=2*c-2*r2+1
        arr=[]
        arr11=[]
        arr12=[]
        arr1=[]
        arr2=[]
        arr3=[]
        arr4=[]
        while (c*x<=y):#0->r2
            arr11.append([x,y,color,x])#0-90
            if (p<0):
                p += 2*c*(2*x+3)
            else:
                p +=4*(1-y)+2*c*(2*x+3)
                y-=1
            x+=1
        x2=x
        y=0;x=r1
        c= r1/r2
        c=c*c; p=2*c-2*r1+1
        while (c*y<=x):
            arr12.append([x,y,color,x2])
            if (p<0):
                p +=2*c*(2*y+3)
            else:
                p +=4*(1-x)+2*c*(2*y+3)
                x-=1
            y+=1
            x2+=1
        
        arr11 = np.array(arr11,dtype=object)
        arr12 = np.array(arr12,dtype=object)
        arr12 = Draw.flip_arr(arr12)
        arr1 = np.concatenate((arr11,arr12))
        # phần tư thứ 2
        x2-=1
        arr2 = np.flip(arr1.copy(),0) # xài copy vì arr1 bị thay đổi
        for x in arr2:
            x[1]=x[1]*-1
            x[3]=x2
            x2+=1
        # phần tư thứ 3
        x2-=1
        arr3 = np.flip(arr2.copy(),0)
        for x in arr3:
            x[0]=x[0]*-1
            x[3]=x2
            x2+=1
        # phần tư thứ 4
        x2-=1
        arr4 = np.flip(arr3.copy(),0)
        for x in arr4:
            x[1]=x[1]*-1
            x[3]=x2
            x2+=1
        arr = np.concatenate((arr1,arr2,arr3,arr4))
        # chuyển hệ số góc
        x2-=1
        for x in arr:
            x[3]=round(x[3]/x2*360)
        arr = Draw.remove_ellipse(arr,start,end)

        return Convert_coordinate.real2mon_arr(arr)
class Bien_doi():
    def phep_quay(arr,x1,y1,a):
        x1,y1 = Convert_coordinate.real2mon(x1,y1)
        """quay arr quanh điểm X1,Y1 với góc quay a"""
        # x2 = x1+cos(a)*(x-x1)-sin(a)*(y1-y)
        # y2 = y1+cos(a)*(y-y1)+sin(a)*(x-x1)
        # x[0] là x, x[1] là y
        # (x-x1)cos(a) – (y-y1)sin(a) + x1
        # (x-x1)sin(a) +  (y-y1)cos(a)+y1
        a = math.radians(a)
        for element in arr:
            x = element[0]; y = element[1]
            element[0]= x1+math.cos(a)*(x-x1)-math.sin(a)*(y-y1) #x*cos(a)-y*sin(a)
            element[1]= y1+math.cos(a)*(y-y1)+math.sin(a)*(x-x1) #y*cos(a)+x*sin(a)
        return Convert_coordinate.round(arr)
    def MT_tinh_tien(x,y):
        return np.array([[1,0,0],[0,1,0],[x,y,1]])
    def MT_ti_le(Sx,Sy):
        return np.array([[Sx,0,0],[0,Sy,0],[0,0,1]])
    def MT_quay(alpha):
        alpha = math.radians(alpha)
        return np.array([[math.cos(alpha),math.sin(alpha),0],[-math.sin(alpha),math.cos(alpha),0],[0,0,1]])
    def MT_doi_xung(type):
        """type =1: Ox | type =2: Oy | type =3: tâm O"""
        if type==1:
            return np.array([[1,0,0],[0,-1,0],[0,0,1]])
        if type==2:
            return np.array([[-1,0,0],[0,1,0],[0,0,1]])
        if type==3:
            return np.array([[-1,0,0],[0,-1,0],[0,0,1]])
    def Nhan_MT(arr,mt):
        for element in arr:
            x = element[0]; y = element[1]
            mt1 = np.array([x,y,1])
            result=np.dot(mt1,mt)
            element[0]= result[0]
            element[1]= result[1]
        return Convert_coordinate.round(arr)