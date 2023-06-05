import pygame

pygame.init()

class Snail():
    def __init__(self):
        self.player_imgs=['graphics/snail/snail1.png','graphics/snail/snail2.png']
        self.img=pygame.image.load(self.player_imgs[0])
        self.rect=self.img.get_rect()
        self.velocity=10
        self.value=-1
    def forward(self,point):
        self.rect.x-=self.velocity
        if self.rect.x<-100:
            self.rect.x=point
    def snail_walk(self):
        self.value+=1
        if self.value==2:
            self.value=0
        self.player_img=pygame.image.load(self.player_imgs[self.value])
        print(self.player_img)
