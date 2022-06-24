from time import sleep
import pygame
import all_func as FC
import pygame_gui
from khaibao import *
import numpy as np
import easygui
import math

pygame.init()
surface = pygame.display.set_mode((250,200))
surface.fill(white_color) # đổi màu background sang trắng
pygame.display.set_caption('Đồ án cuối kì')
manager = pygame_gui.UIManager((250,200))

bt_2D = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(35,10,180,30),# (x bắt đầu, y bắt đầu, width, height)
                            text='2D',
                            manager=manager
                        )
bt_3D1 = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(35,50,180,30),# (x bắt đầu, y bắt đầu, width, height)
                            text='3D - Hinh Hop CN',
                            manager=manager
)
bt_3D2 = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(35,90,180,30),# (x bắt đầu, y bắt đầu, width, height)
                            text='3D - Hinh Tru',
                            manager=manager
)
def clear_screen(isGrid,isXY):
    """isGrid: True or False | isXY: 0 là ko có, 1 là XY, 2 là XYZ"""
    surface.fill(white_color)  # đổi màu background sang trắng
    # pygame.draw.rect(surface,red_color,pygame.Rect(0, 0, 1000, 600))
    if(isGrid):
        FC.Draw_grid(surface, manager, start_x, end_x, start_y, end_y)
    if(isXY==1):
        FC.Draw_grid.xy(surface, manager, start_x, end_x, start_y, end_y)
    elif(isXY==2):
        FC.Draw_grid.xyz(surface, manager, start_x, end_x, start_y, end_y)
isRunning = True
isGrid =True
clock = pygame.time.Clock()
def do_an_2D(isGrid):
    manager = pygame_gui.UIManager((end_x+manager_x, end_y+20))
    # Toạ độ kết thúc của lưới toạ độ

    surface = pygame.display.set_mode(
        (end_x+manager_x, end_y+20))  # tạo cửa sổ #1180x620
    surface.fill(white_color)  # đổi màu background sang trắng
    pygame.display.set_caption('2D')  # Tên của sổ
    # width,height
    background = pygame.Surface((manager_x, 170))  # Tạo phần điều khiển
    background.fill(gray_black_color)  # background của phần điều khiển

    background1 = pygame.Surface((end_x+20, 20))  # Tạo phần điều khiển
    background1.fill(white_color)  # background của phần điều khiển

    background2 = pygame.Surface((end_x+19, 20))  # Tạo phần điều khiển
    background2.fill(white_color)  # background của phần điều khiển

    background3 = pygame.Surface((20, grid_y))  # Tạo phần điều khiển
    background3.fill(white_color)  # background của phần điều khiển

    background4 = pygame.Surface((19, grid_y))  # Tạo phần điều khiển
    background4.fill(white_color)  # background của phần điều khiển


    #############Phần điều khiển####################
    bt_DX_Ox = pygame_gui.elements.UIButton(
        # (x bắt đầu, y bắt đầu, width, height)
        relative_rect=pygame.Rect(manager_x_axis+5, 10, 150, 30),
        text='Doi xung Ox',
        manager=manager
    )
    bt_DX_Oy = pygame_gui.elements.UIButton(
        # (x bắt đầu, y bắt đầu, width, height)
        relative_rect=pygame.Rect(manager_x_axis+5, 50, 150, 30),
        text='Doi xung Oy',
        manager=manager
    )
    bt_DX_O = pygame_gui.elements.UIButton(
        # (x bắt đầu, y bắt đầu, width, height)
        relative_rect=pygame.Rect(manager_x_axis+5, 90, 150, 30),
        text='Doi xung tam O',
        manager=manager
    )
    bt_clear = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(manager_x_axis+5, 130, 150, 30),
        text='Bat/Tat grid',
        manager=manager
    )
    ##################################################
    isRunning = True
    clock = pygame.time.Clock()
    #################################### DORAEMON #######################################
    face = FC.Draw.ellipse_2(20, 20, blue_color, 0, 140)
    face = np.concatenate((face, FC.Draw.ellipse_2(20, 20, black_color, 220, 335), FC.Draw.ellipse_2(
        20, 20, blue_color, 336, 360), FC.Draw.rect(-12, -16, 12, -18, red_color)))
    mat = FC.Draw.ellipse_2(20, 25, blue_color, 35, 125)
    mat = FC.Bien_doi.Nhan_MT(mat, FC.Bien_doi.MT_tinh_tien(-100, 20))
    eye = FC.Draw.ellipse_2(3, 5, black_color, 40, 230)
    eye = FC.Bien_doi.phep_quay(eye, 0, 0, 20)
    eye = FC.Bien_doi.Nhan_MT(eye, FC.Bien_doi.MT_tinh_tien(-50, -75))
    x_eye, y_eye = FC.Convert_coordinate.real2mon(-11, 14)
    dau = np.concatenate((face, mat, eye, [[x_eye, y_eye, black_color]]))
    dau = FC.Bien_doi.phep_quay(dau, 0, 0, -20)
    mui = FC.Draw.circle_fill(-19, 8, 2, red_color, red_color)
    mong = FC.Draw.ellipse_2(20, 15, blue_color, 25, 80)
    mong = FC.Bien_doi.Nhan_MT(mong, FC.Bien_doi.MT_tinh_tien(50, 140))
    bung = FC.Draw.ellipse_2(20, 15, black_color, 180, 300)
    bung = FC.Bien_doi.Nhan_MT(bung, FC.Bien_doi.MT_tinh_tien(70, 140))
    chan = FC.Draw.line(15, -43, 30, -42, blue_color)
    chan = np.concatenate((chan, FC.Draw.line(30, -25, 32, -26, blue_color),
                        FC.Draw.ellipse_fill(35, -35, 6, 8, black_color, white_color)))  # ban chan 792
    chuong = FC.Draw.circle_fill(-6, -20, 2, yellow_color, yellow_color)  # 192
    tay = FC.Draw.line(3, -21, 8, -14, black_color)
    tay = np.concatenate((tay, FC.Draw.line(13, -24, 15, -17, black_color),  # 45
                        FC.Draw.circle_fill(13, -13, 4, black_color, white_color)))  # 621
    bung_duoi = FC.Draw.ellipse_2(20, 15, black_color, 0, 100)
    bung_duoi = FC.Bien_doi.Nhan_MT(
        bung_duoi, FC.Bien_doi.MT_tinh_tien(-25, 200))  # 93
    tui = FC.Draw.ellipse_2(8, 8, black_color, 30, 100)
    tui = FC.Bien_doi.Nhan_MT(tui, FC.Bien_doi.MT_tinh_tien(0, 200))
    tui = np.concatenate((tui, FC.Draw.line(0, -37, 4, -33, black_color)))
    duoi = np.concatenate((FC.Draw.circle_fill(36, -18, 2, red_color, red_color),
                        FC.Draw.line(33, -20, 30, -22, black_color)))  # 204
    chong_chong = FC.Draw.ellipse_2(3, 3, yellow_color, 0, 120)
    chong_chong = np.concatenate(
        (chong_chong, FC.Draw.ellipse_2(3, 3, yellow_color, 270, 360)))
    chong_chong = FC.Bien_doi.Nhan_MT(
        chong_chong, FC.Bien_doi.MT_tinh_tien(30, -100))
    chong_chong = np.concatenate(
        (chong_chong, FC.Draw.line(7, 23, 8, 28, yellow_color)))
    canh_quat = FC.Draw.ellipse_2(6, 3, black_color, 0, 360)
    canh_quat = FC.Bien_doi.phep_quay(canh_quat, 0, 0, 10)
    canh_quat = FC.Bien_doi.Nhan_MT(canh_quat, FC.Bien_doi.MT_tinh_tien(40, -140))
    chong_chong = np.concatenate((chong_chong, canh_quat))  # 153
    mieng = FC.Draw.ellipse_2(10, 10, black_color, 90, 160)
    mieng = FC.Bien_doi.Nhan_MT(mieng, FC.Bien_doi.MT_tinh_tien(-90, 20))
    chi_tiet_mat = np.concatenate((mui, mieng, FC.Draw.line(-8, 0, 1, 6, black_color),
                                FC.Draw.line(-5, -3, 5, 2,
                                                black_color), FC.Draw.line(-4, -6, 5, -4, black_color),
                                chuong, chong_chong))  # 669
    phan_than = np.concatenate((mong, bung, chan, duoi, bung_duoi))  # 1305
    linh_kien = np.concatenate((tui, tay))  # 666
    doraemon = np.concatenate((dau, phan_than, linh_kien, chi_tiet_mat))  # 3237
    #################################### MAY #######################################
    may = FC.Draw.ellipse_2(6, 5, pink_dark_color, 0, 120)
    may = FC.Bien_doi.Nhan_MT(may, FC.Bien_doi.MT_tinh_tien(0, 25))
    may1 = FC.Draw.ellipse_2(12, 12, pink_dark_color, 0, 160)
    may1 = FC.Bien_doi.Nhan_MT(may1, FC.Bien_doi.MT_tinh_tien(25, 100))
    may2 = FC.Draw.ellipse_2(8, 8, pink_dark_color, 80, 180)
    may2 = FC.Bien_doi.Nhan_MT(may2, FC.Bien_doi.MT_tinh_tien(0, 160))
    may = np.concatenate(
        (may, may1, may2, FC.Draw.line(0, 0, 0, -40, pink_dark_color)))
    may = FC.Bien_doi.phep_quay(may, 0, 0, -90)
    # may = FC.Bien_doi.Nhan_MT(may,FC.Bien_doi.MT_tinh_tien(0,-200))
    a, b = FC.Convert_coordinate.real2mon(20, 3)
    may_to_mau = []
    FC.Put_pixel(surface, may)
    may_to_mau = FC.To_mau.loang(
        surface, a, b, pink_dark_color, pink_color, may_to_mau)
    may = np.concatenate((may, may_to_mau))
    may_animation = np.copy(may)
    may_animation = FC.Bien_doi.Nhan_MT(
        may_animation, FC.Bien_doi.MT_tinh_tien(-700, -190))
    # mattroi
    sun = FC.Draw.circle_fill(-70, 40, 15, orange_color_sun, orange_color_sun)
    # nui
    nui = FC.Draw.line(0, 0, 40, 50, black_color)
    nui = np.concatenate((nui, FC.Draw.line(
        80, 0, 40, 50, black_color), FC.Draw.line(0, 0, 80, 0, black_color)))
    nui = FC.Bien_doi.Nhan_MT(nui, FC.Bien_doi.MT_tinh_tien(-620, 100))

    nui1 = FC.Draw.line(17, 24, 25, 35, black_color)
    nui1 = np.concatenate((nui1, FC.Draw.line(
        50, 0, 25, 35, black_color), FC.Draw.line(0, 0, 50, 0, black_color)))
    nui1 = FC.Bien_doi.Nhan_MT(nui1, FC.Bien_doi.MT_tinh_tien(-400, 100))
    # sunshine
    sunshine1 = FC.Draw.line(0, 20, 0, 25, orange_color_sun)
    sunshine1 = np.concatenate((sunshine1, FC.Draw.line(0, -20, 0, -25, orange_color_sun),
                                FC.Draw.line(-20, 0, -25, 0, orange_color_sun), FC.Draw.line(20, 0, 25, 0, orange_color_sun)))
    sunshine1 = np.concatenate((sunshine1, FC.Draw.line(15, 15, 19, 19, orange_color_sun), FC.Draw.line(-15, 15, -19, 19, orange_color_sun),
                                FC.Draw.line(15, -15, 19, -19, orange_color_sun), FC.Draw.line(-15, -15, -19, -19, orange_color_sun)))
    sunshine1 = FC.Bien_doi.Nhan_MT(
        sunshine1, FC.Bien_doi.MT_tinh_tien(-350, -200))
    temp_sunshine1 = np.copy(sunshine1)
    count = 0
    bool = 5
    alpha = 10
    scale_x = 1
    scale_y = 1
    step = 0
    may_step = 0
    may_move_dir = 5
    is_scale_up = True
    font = pygame.font.SysFont(None, 24)
    while isRunning:
        time_delta = clock.tick(24)/1000.0
        if (isGrid):
            FC.Draw_grid(surface, manager, start_x, end_x, start_y, end_y)
        FC.Draw_grid.xy(surface, manager, start_x, end_x, start_y, end_y)
        count += 1
        if (count > 12):
            bool = -bool
            count = 0
        doraemon = FC.Bien_doi.Nhan_MT(doraemon, FC.Bien_doi.MT_tinh_tien(0, bool))
        FC.Put_pixel(surface, nui)
        FC.Put_pixel(surface, nui1)
        # sunshine logic
        sunshine = FC.Bien_doi.phep_quay(temp_sunshine1, -70, 40, alpha)
        temp_sunshine1 = np.copy(sunshine1)
        alpha += 5
        #####

        ####may logic###
        if(may_step == 240):
            may_animation = FC.Bien_doi.Nhan_MT(
                may_animation, FC.Bien_doi.MT_tinh_tien(-(may_step*may_move_dir), 0))
            may_step = 0
        may_animation = FC.Bien_doi.Nhan_MT(
            may_animation, FC.Bien_doi.MT_tinh_tien(may_move_dir, 0))
        may_step += 1
        ####ty le###
        step += 1
        if (step > 4 and is_scale_up):
            scale_x = 0.95
            scale_y = 0.95
            step = 0
            is_scale_up = False
        if (step > 1 and not is_scale_up):
            scale_x = 1
            scale_y = 1
            sun = FC.Draw.circle_fill(-70, 40, 15,
                                    orange_color_sun, orange_color_sun)
            step = 0
            is_scale_up = True
        ox, oy = FC.Convert_coordinate.real2mon(-70, 40)
        mt_bien_doi_ty_le = np.dot(
            FC.Bien_doi.MT_tinh_tien(-ox, -oy), FC.Bien_doi.MT_ti_le(scale_x, scale_y))
        mt_bien_doi_ty_le = np.dot(
            mt_bien_doi_ty_le, FC.Bien_doi.MT_tinh_tien(ox, oy))
        sun = FC.Bien_doi.Nhan_MT(sun, mt_bien_doi_ty_le)
        FC.Put_pixel(surface, sunshine)
        FC.Put_pixel(surface, sun)
        FC.Put_pixel(surface, may_animation)
        FC.Put_pixel(surface, doraemon)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == bt_DX_Ox:
                        ox, oy = FC.Convert_coordinate.real2mon(0, 0)
                        mt_bien_doi = np.dot(
                            FC.Bien_doi.MT_tinh_tien(-ox, -oy), FC.Bien_doi.MT_doi_xung(1))
                        mt_bien_doi = np.dot(
                            mt_bien_doi, FC.Bien_doi.MT_tinh_tien(ox, oy))
                        doraemon = FC.Bien_doi.Nhan_MT(doraemon, mt_bien_doi)
                    if event.ui_element == bt_DX_Oy:
                        may_step = 200-may_step
                        may_move_dir = -may_move_dir
                        ox, oy = FC.Convert_coordinate.real2mon(0, 0)
                        mt_bien_doi = np.dot(
                            FC.Bien_doi.MT_tinh_tien(-ox, -oy), FC.Bien_doi.MT_doi_xung(2))
                        mt_bien_doi = np.dot(
                            mt_bien_doi, FC.Bien_doi.MT_tinh_tien(ox, oy))
                        doraemon = FC.Bien_doi.Nhan_MT(doraemon, mt_bien_doi)
                    if event.ui_element == bt_DX_O:
                        ox, oy = FC.Convert_coordinate.real2mon(0, 0)
                        mt_bien_doi = np.dot(
                            FC.Bien_doi.MT_tinh_tien(-ox, -oy), FC.Bien_doi.MT_doi_xung(3))
                        mt_bien_doi = np.dot(
                            mt_bien_doi, FC.Bien_doi.MT_tinh_tien(ox, oy))
                        doraemon = FC.Bien_doi.Nhan_MT(doraemon, mt_bien_doi)
                    if event.ui_element == bt_clear:
                        isGrid = not(isGrid)
            manager.process_events(event)
        ################################################################
        img = font.render("THONG SO", True, black_color)
        surface.blit(img, (1020, 180))
        headX, headY = FC.Convert_coordinate.mon2real(
            doraemon[1, 0], doraemon[1, 1])
        toadoHead = "%d,%d" % (headX+6, headY-20)
        img = font.render("Head        " + toadoHead, True, black_color)
        surface.blit(img, (1020, 200))

        muiX, muiY = FC.Convert_coordinate.mon2real(
            doraemon[856, 0], doraemon[856, 1])
        toadoMui = "%d,%d" % (muiX, muiY-2)
        img = font.render("Nose        " + toadoMui, True, black_color)
        surface.blit(img, (1020, 220))

        # 964
        chuongX, chuongY = FC.Convert_coordinate.mon2real(
            doraemon[964, 0], doraemon[964, 1])
        toadoChuong = "%d,%d" % (chuongX, chuongY-2)
        img = font.render("Bell        " + toadoChuong, True, black_color)
        surface.blit(img, (1020, 240))

        # 664
        tayX, tayY = FC.Convert_coordinate.mon2real(
            doraemon[664, 0], doraemon[664, 1])
        toadoTay = "%d,%d" % (tayX, tayY-4)
        img = font.render("Hand        " + toadoTay, True, black_color)
        surface.blit(img, (1020, 260))

        # 535
        duoiX, duoiY = FC.Convert_coordinate.mon2real(
            doraemon[535, 0], doraemon[535, 1])
        toadoDuoi = "%d,%d" % (duoiX, duoiY-2)
        img = font.render("Tail        " + toadoDuoi, True, black_color)
        surface.blit(img, (1020, 280))
        # 271
        chanX, chanY = FC.Convert_coordinate.mon2real(
            doraemon[271, 0], doraemon[271, 1])
        toadoChan = "%d,%d" % (chanX-2, chanY-8)
        img = font.render("Foot        " + toadoChan, True, black_color)
        surface.blit(img, (1020, 300))

        sunX, sunY = FC.Convert_coordinate.mon2real(-70, 40)
        toadoSun = "%d,%d" % (sunX, sunY)
        img = font.render("Sun        " + toadoSun, True, black_color)
        surface.blit(img, (1020, 320))
        # 80
        cloudX, cloudY = FC.Convert_coordinate.mon2real(
            may_animation[80, 0], may_animation[80, 1])
        toadoCloud = "%d,%d" % (cloudX, cloudY)
        img = font.render("Cloud        " + toadoCloud, True, black_color)
        surface.blit(img, (1020, 340))
        # 80
        nuiX, nuiY = FC.Convert_coordinate.mon2real(-360, -100)
        toadoNui = "%d,%d" % (nuiX, nuiY)
        img = font.render("Mountain     " + toadoNui, True, black_color)
        surface.blit(img, (1020, 360))
        surface.blit(background, (manager_x_axis, 0))  # ghi đè lên cửa sổ
        surface.blit(background1, (0, 0))  # thanh bên trên
        surface.blit(background2, (0, grid_y+21))  # thanh bên dưới
        surface.blit(background3, (0, 20))  # thanh bên trái
        surface.blit(background4, (grid_x+21, 20))  # thanh bên phải
        manager.update(time_delta)
        manager.draw_ui(surface)
        pygame.display.flip()
        clock.tick(24)
        clear_screen(isGrid,1)
    clear_screen(0,0)
def do_an_3D_1(isGrid):
    manager = pygame_gui.UIManager((end_x+manager_x,end_y+20))
    #Toạ độ kết thúc của lưới toạ độ

    surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ #1180x620
    surface.fill(white_color) # đổi màu background sang trắng
    pygame.display.set_caption('3D - hình hộp chữ nhật') #Tên của sổ
    background = pygame.Surface((manager_x,380))#Tạo phần điều khiển
    background.fill(gray_black_color) #background của phần điều khiển

    background1 = pygame.Surface((end_x+20,20))#Tạo phần điều khiển
    background1.fill(white_color) #background của phần điều khiển

    background2 = pygame.Surface((end_x+19,20))#Tạo phần điều khiển
    background2.fill(white_color) #background của phần điều khiển

    background3 = pygame.Surface((20,grid_y))#Tạo phần điều khiển
    background3.fill(white_color) #background của phần điều khiển

    background4 = pygame.Surface((19,grid_y))#Tạo phần điều khiển
    background4.fill(white_color) #background của phần điều khiển
    #############Phần điều khiển####################
    bt_line = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect(manager_x_axis+5,260,150,30),
                                text='Ve hinh',
                                manager=manager
                            )
    X_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,20,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,20,40,30),
                                text="X",
                                manager=manager)
    Y_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,60,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,60,40,30),
                                text="Y",
                                manager=manager)
    Z_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,100,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,100,40,30),
                                text="Z",
                                manager=manager)
    L_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,140,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,140,40,30),
                                text="Dai",
                                manager=manager)
    W_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,180,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,180,40,30),
                                text="Rong",
                                manager=manager)
    H_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,220,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,220,40,30),
                                text="Cao",
                                manager=manager)

    bt_clear = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect(manager_x_axis+5,300,150,30),
                                text='Clear',
                                manager=manager
                            )
    bt_grid = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect(manager_x_axis+5,340,150,30),
                                text='Bat/Tat grid',
                                manager=manager
                            )
    ##################################################
    isRunning = True
    clock = pygame.time.Clock()
    FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
    FC.Draw_grid.xyz(surface,manager,start_x,end_x,start_y,end_y)
    while isRunning:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    try:
                        if event.ui_element == bt_line:
                            arr=[]
                            x=int(X_axis.get_text())
                            y=int(Y_axis.get_text())
                            z=int(Z_axis.get_text())
                            l=int(L_axis.get_text())
                            h=int(H_axis.get_text())
                            w=int(W_axis.get_text())
                            # A,B,C,D,E,F,G,H
                            # A(a1,a2)
                            # B(b1,b2)
                            #  ......
                            a1,a2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y,z)
                            b1,b2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y+h,z)
                            c1,c2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y+h,z)
                            d1,d2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y,z)
                            e1,e2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y,z+l)
                            f1,f2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y+h,z+l)
                            g1,g2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y+h,z+l)
                            h1,h2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y,z+l)

                            xA,yA = FC.Convert_coordinate.real2mon(a1,a2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('A', True, orange_color)
                            surface.blit(img, (xA+10, yA-20))
                            img = font.render("THONG SO", True, black_color)
                            surface.blit(img, (1050, 390))
                            toadoA = "%d,%d,%d" %(x,y,z)
                            img = font.render("A        " + toadoA, True, black_color)
                            surface.blit(img, (1050, 410))

                            xB,yB = FC.Convert_coordinate.real2mon(b1,b2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('B', True, orange_color)
                            surface.blit(img, (xB+10, yB-20))
                            toadoB = "%d,%d,%d" %(x,y+h,z)
                            img = font.render("B        " + toadoB, True, black_color)
                            surface.blit(img, (1050, 430))

                            xC,yC = FC.Convert_coordinate.real2mon(c1,c2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('C', True, orange_color)
                            surface.blit(img, (xC+10, yC-20))
                            toadoC = "%d,%d,%d" %(x+w,y+h,z)
                            img = font.render("C        " + toadoC, True, black_color)
                            surface.blit(img, (1050, 450))

                            xD,yD = FC.Convert_coordinate.real2mon(d1,d2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('D', True, orange_color)
                            surface.blit(img, (xD+10, yD-20))
                            toadoD = "%d,%d,%d" %(x+w,y,z)
                            img = font.render("D        " + toadoD, True, black_color)
                            surface.blit(img, (1050, 470))

                            xE,yE = FC.Convert_coordinate.real2mon(e1,e2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('E', True, orange_color)
                            surface.blit(img, (xE-20, yE+10))
                            toadoE = "%d,%d,%d" %(x,y,z+l)
                            img = font.render("E        " + toadoE, True, black_color)
                            surface.blit(img, (1050, 490))

                            xF,yF = FC.Convert_coordinate.real2mon(f1,f2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('F', True, orange_color)
                            surface.blit(img, (xF-20, yF+10))
                            toadoF = "%d,%d,%d" %(x,y+h,z+l)
                            img = font.render("F        " + toadoF, True, black_color)
                            surface.blit(img, (1050, 510))

                            xG,yG = FC.Convert_coordinate.real2mon(g1,g2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('G', True, orange_color)
                            surface.blit(img, (xG-20, yG+10))
                            toadoG = "%d,%d,%d" %(x+w,y+h,z+l)
                            img = font.render("G        " + toadoG, True, black_color)
                            surface.blit(img, (1050, 530))

                            xH,yH = FC.Convert_coordinate.real2mon(h1,h2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('H', True, orange_color)
                            surface.blit(img, (xH-20, yH+10))
                            toadoH = "%d,%d,%d" %(x+w,y,z+l)
                            img = font.render("H        " + toadoH, True, black_color)
                            surface.blit(img, (1050, 550))

                            arr = FC.Draw.line(a1,a2,b1,b2,red_color,1)#AB
                            arr = np.concatenate((arr,FC.Draw.line(c1,c2,b1,b2,red_color)))#BC
                            arr = np.concatenate((arr,FC.Draw.line(c1,c2,d1,d2,red_color)))#CD
                            arr = np.concatenate((arr,FC.Draw.line(a1,a2,d1,d2,red_color,1)))#AD
                            arr = np.concatenate((arr,FC.Draw.line(a1,a2,e1,e2,red_color,1)))#AE
                            arr = np.concatenate((arr,FC.Draw.line(e1,e2,h1,h2,red_color)))#EH
                            arr = np.concatenate((arr,FC.Draw.line(d1,d2,h1,h2,red_color)))#DH
                            arr = np.concatenate((arr,FC.Draw.line(b1,b2,f1,f2,red_color)))#BF
                            arr = np.concatenate((arr,FC.Draw.line(f1,f2,g1,g2,red_color)))#FG
                            arr = np.concatenate((arr,FC.Draw.line(g1,g2,c1,c2,red_color)))#GC
                            arr = np.concatenate((arr,FC.Draw.line(e1,e2,f1,f2,red_color)))#EF
                            arr = np.concatenate((arr,FC.Draw.line(g1,g2,h1,h2,red_color)))#GH
                            arr = np.concatenate((arr,FC.Draw.line(d1,d2,c1,c2,red_color)))#DC

                            FC.Put_pixel(surface,arr)
                            FC.Put_pixel.point(surface,xA,yA,orange_color)
                            FC.Put_pixel.point(surface,xB,yB,orange_color)
                            FC.Put_pixel.point(surface,xC,yC,orange_color)
                            FC.Put_pixel.point(surface,xD,yD,orange_color)
                            FC.Put_pixel.point(surface,xE,yE,orange_color)
                            FC.Put_pixel.point(surface,xF,yF,orange_color)
                            FC.Put_pixel.point(surface,xG,yG,orange_color)
                            FC.Put_pixel.point(surface,xH,yH,orange_color)

                        if event.ui_element == bt_clear:
                            clear_screen(isGrid,2)
                        if event.ui_element == bt_grid:
                            isGrid = not(isGrid)
                            clear_screen(isGrid,2)
                    except ValueError:
                        easygui.msgbox("X and Y not be empty", title="ERROR")
            manager.process_events(event)
        surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ
        surface.blit(background1,(0,0))#thanh bên trên
        surface.blit(background2,(0,grid_y+21))#thanh bên dưới
        surface.blit(background3,(0,20))#thanh bên trái
        surface.blit(background4,(grid_x+21,20))#thanh bên phải
        manager.update(time_delta)
        manager.draw_ui(surface)
        pygame.display.flip()
    clear_screen(0,0)

def do_an_3D_2(isGrid):
    manager = pygame_gui.UIManager((end_x+manager_x,end_y+20))
    #Toạ độ kết thúc của lưới toạ độ

    surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ #1180x620
    surface.fill(white_color) # đổi màu background sang trắng
    pygame.display.set_caption('3D - Hình trụ') #Tên của sổ
    background = pygame.Surface((manager_x,350))#Tạo phần điều khiển
    background.fill(gray_black_color) #background của phần điều khiển

    background1 = pygame.Surface((end_x+20,20))#Tạo phần điều khiển
    background1.fill(white_color) #background của phần điều khiển

    background2 = pygame.Surface((end_x+19,20))#Tạo phần điều khiển
    background2.fill(white_color) #background của phần điều khiển

    background3 = pygame.Surface((20,grid_y))#Tạo phần điều khiển
    background3.fill(white_color) #background của phần điều khiển

    background4 = pygame.Surface((19,grid_y))#Tạo phần điều khiển
    background4.fill(white_color) #background của phần điều khiển
    #############Phần điều khiển####################
    bt_line = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect(manager_x_axis+5,220,150,30),
                                text='Ve hinh tru',
                                manager=manager
                            )
    X_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,20,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,20,40,30),
                                text="X",
                                manager=manager)
    Y_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,60,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,60,40,30),
                                text="Y",
                                manager=manager)
    Z_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,100,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,100,40,30),
                                text="Z",
                                manager=manager)
    R_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+100,140,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,140,80,30),
                                text="Ban kinh",
                                manager=manager)
    H_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+100,180,40,30),
                                manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,180,80,30),
                                text="Chieu cao",
                                manager=manager)

    bt_clear = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect(manager_x_axis+5,260,150,30),
                                text='Clear',
                                manager=manager
                            )
    bt_grid = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect(manager_x_axis+5,300,150,30),
                                text='Bat/Tat grid',
                                manager=manager
                            )
    ##################################################
    clock = pygame.time.Clock()
    FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
    FC.Draw_grid.xyz(surface,manager,start_x,end_x,start_y,end_y)
    isRunning= True
    while isRunning:
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    try:
                        if event.ui_element == bt_line:
                            arr=[]
                            x=int(X_axis.get_text())
                            y=int(Y_axis.get_text())
                            z=int(Z_axis.get_text())
                            h=int(H_axis.get_text())
                            r=int(R_axis.get_text())
                        
                            a1,a2 = FC.Convert_coordinate.Chuyen_3Dto2D(x-r,y,z)
                            b1,b2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+r,y,z)
                            c1,c2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+r,y+h,z)
                            d1,d2 = FC.Convert_coordinate.Chuyen_3Dto2D(x-r,y+h,z)
                            g1,g2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y,z)
                            h1,h2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y+h,z)

                            xA,yA = FC.Convert_coordinate.real2mon(a1,a2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('A', True, orange_color)
                            surface.blit(img, (xA-20, yA))
                            img = font.render("THONG SO", True, black_color)
                            surface.blit(img, (1050, 390))
                            toadoA = "%d,%d,%d" %(x-r,y,z)
                            img = font.render("A        " + toadoA, True, black_color)
                            surface.blit(img, (1050, 410))

                            xB,yB = FC.Convert_coordinate.real2mon(b1,b2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('B', True, orange_color)
                            surface.blit(img, (xB+10, yB))
                            toadoB = "%d,%d,%d" %(x+r,y,z)
                            img = font.render("B        " + toadoB, True, black_color)
                            surface.blit(img, (1050, 430))

                            xC,yC = FC.Convert_coordinate.real2mon(c1,c2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('C', True, orange_color)
                            surface.blit(img, (xC+10, yC))
                            toadoC = "%d,%d,%d" %(x+r,y+h,z)
                            img = font.render("C        " + toadoC, True, black_color)
                            surface.blit(img, (1050, 450))

                            xD,yD = FC.Convert_coordinate.real2mon(d1,d2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('D', True, orange_color)
                            surface.blit(img, (xD-20, yD))
                            toadoD = "%d,%d,%d" %(x-r,y+h,z)
                            img = font.render("D        " + toadoD, True, black_color)
                            surface.blit(img, (1050, 470))

                            xG,yG = FC.Convert_coordinate.real2mon(g1,g2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('G', True, orange_color)
                            surface.blit(img, (xG-20, yG))
                            toadoG = "%d,%d,%d" %(x,y,z)
                            img = font.render("G        " + toadoG, True, black_color)
                            surface.blit(img, (1050, 490))

                            xH,yH = FC.Convert_coordinate.real2mon(h1,h2)
                            font = pygame.font.SysFont(None, 24)
                            img = font.render('H', True, orange_color)
                            surface.blit(img, (xH-20, yH))
                            toadoH = "%d,%d,%d" %(x,y+h,z)
                            img = font.render("H        " + toadoH, True, black_color)
                            surface.blit(img, (1050, 510))

                            bankinhnho = int(r*(math.sqrt(2) / 2))

                            arr1 = FC.Draw.ellipse(g1,g2,r,bankinhnho,red_color,1)
                            arr1 = np.concatenate((arr1,FC.Draw.ellipse(h1,h2,r,bankinhnho,red_color)))

                            arr = FC.Draw.line(a1,a2,d1,d2,red_color)#AD
                            arr = np.concatenate((arr,FC.Draw.line(c1,c2,b1,b2,red_color)))#BC
                            arr = np.concatenate((arr,FC.Draw.line(h1,h2,c1,c2,red_color)))#HC
                            arr = np.concatenate((arr,FC.Draw.line(g1,g2,b1,b2,red_color,1)))#GB
                            arr = np.concatenate((arr,FC.Draw.line(h1,h2,g1,g2,red_color,1)))#HG

                            FC.Put_pixel(surface,arr)
                            FC.Put_pixel(surface,arr1)
                            FC.Put_pixel.point(surface,xA,yA,orange_color)
                            FC.Put_pixel.point(surface,xB,yB,orange_color)
                            FC.Put_pixel.point(surface,xC,yC,orange_color)
                            FC.Put_pixel.point(surface,xD,yD,orange_color)
                            FC.Put_pixel.point(surface,xG,yG,orange_color)
                            FC.Put_pixel.point(surface,xH,yH,orange_color)

                        if event.ui_element == bt_clear:
                            clear_screen(isGrid,2)
                        if event.ui_element == bt_grid:
                            isGrid = not(isGrid)
                            clear_screen(isGrid,2)
                    except ValueError:
                        easygui.msgbox("X and Y not be empty", title="ERROR")
            manager.process_events(event)
        surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ
        surface.blit(background1,(0,0))#thanh bên trên
        surface.blit(background2,(0,grid_y+21))#thanh bên dưới
        surface.blit(background3,(0,20))#thanh bên trái
        surface.blit(background4,(grid_x+21,20))#thanh bên phải
        manager.update(time_delta)
        manager.draw_ui(surface)
        pygame.display.flip()
    clear_screen(0,0)
while isRunning:
    time_delta = clock.tick(24)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bt_2D:
                    do_an_2D(isGrid)
                if event.ui_element == bt_3D1:
                    do_an_3D_1(isGrid)
                if event.ui_element == bt_3D2:
                    do_an_3D_2(isGrid)
                #trả lại trạng thái ban đầu
                surface = pygame.display.set_mode((250,200))
                surface.fill(white_color) # đổi màu background sang trắng
                pygame.display.set_caption('Đồ án cuối kì')
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.flip()
    clock.tick(24)
    # clear_screen(isGrid)