import pygame
import random
from block import Block

class Food():
    def __init__(self,surface,size,col,row):
        self.surface=surface
        self.size=size
        self.col=col
        self.row=row
        x=random.randint(0,col-1)
        y=random.randint(0,row-1)
        self.block=Block(x,y)
    def draw_food(self):
        self.rect=pygame.Rect(self.block.x*self.size,self.block.y*self.size,self.size,self.size)
        pygame.draw.rect(self.surface,pygame.Color("red"),self.rect)
        