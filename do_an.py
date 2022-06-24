import pygame
import pygame_gui
from khaibao import *
pygame.init()
surface = pygame.display.set_mode((250,200)) #tạo cửa sổ #1180x620
surface.fill(white_color) # đổi màu background sang trắng
manager = pygame_gui.UIManager((250,200))

bt_DX_Ox = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(50,10,150,30),# (x bắt đầu, y bắt đầu, width, height)
                            text='Doi xung Ox',
                            manager=manager
                        )
bt_DX_Oy = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(50,50,150,30),# (x bắt đầu, y bắt đầu, width, height)
                            text='Doi xung Oy',
                            manager=manager
)
bt_DX_O = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(50,90,150,30),# (x bắt đầu, y bắt đầu, width, height)
                            text='Doi xung tam O',
                            manager=manager
)
bt_clear = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(50,130,150,30),
                            text='Bat/Tat grid',
                            manager=manager
                        )

isRunning = True
clock = pygame.time.Clock()

while isRunning:
    time_delta = clock.tick(24)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bt_DX_Ox:
                    pass
                if event.ui_element == bt_DX_Oy:
                    pass
                if event.ui_element == bt_DX_O:
                    pass
                if event.ui_element == bt_clear:
                    pass
        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.flip()