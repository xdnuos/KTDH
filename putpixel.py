import convert_pixel as CP
import pygame
_UNIT=5
white_color = (255,255,255)
class Put_pixel:
    def __init__(self,surface,x,y,color):
        modulo_x=x%_UNIT
        modulo_y=y%_UNIT
        pygame.draw.rect(surface, color, pygame.Rect(x+modulo_x, y+modulo_y, _UNIT, _UNIT))
    def delete(surface,x,y):
        modulo_x=x%_UNIT
        modulo_y=y%_UNIT
        pygame.draw.rect(surface, white_color, pygame.Rect(x+modulo_x, y+modulo_y, _UNIT, _UNIT))
    def revert(surface,x,y,color):
        new_x,new_y=CP.revert_coordinate_axis(x,y)
        modulo_x=new_x%_UNIT
        modulo_y=new_y%_UNIT
        pygame.draw.rect(surface, color, pygame.Rect(new_x+modulo_x, new_y+modulo_y, _UNIT, _UNIT))