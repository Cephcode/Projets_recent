import pygame

pygame.init()

class Bird():
    def __init__(self):
        self.img=pygame.image.load("graphics/Fly/Fly1.png")
        self.rect=self.img.get_rect()
        self.velocity=12
    def forward(self):
        self.rect.x-=self.velocity
        if self.rect.x<-100:
            self.rect.x=2500