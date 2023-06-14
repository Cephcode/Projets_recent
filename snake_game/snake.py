import pygame
from block import Block
class Snake():
    def __init__(self,surface,size):
        self.body=[Block(2,6),Block(3,6),Block(4,6)]
        self.size=size
        self.surface=surface
        self.direction="right"

    def draw_snake(self):
        for block in self.body:
            x=block.x*self.size
            y=block.y*self.size
            rect=pygame.Rect(x,y,self.size,self.size)
            pygame.draw.rect(self.surface,pygame.Color("green"),rect)

    def move_snake(self):
        snake_block_count=len(self.body)
        old_head=self.body[snake_block_count-1]
        new_head=int
        if self.direction=="right":
            new_head=Block(old_head.x+1,old_head.y)
            # self.body.append(new_head)
            # self.body.pop(0)
        elif self.direction=="left":
            new_head=Block(old_head.x-1,old_head.y)
            print(new_head.x)
            # self.body.append(new_head)
            # print(self.body.index(new_head),self.body.index(old_head))
            # self.body.pop(0)
        elif self.direction=="top":
            new_head=Block(old_head.x,old_head.y-1)
            # self.body.append(new_head)
            # self.body.pop(0)
        elif self.direction=="down":
            new_head=Block(old_head.x,old_head.y+1)
            # self.body.append(new_head)
            # # self.body.pop(0)
        self.body.append(new_head)
        # self.body.pop(0)

