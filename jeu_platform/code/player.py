import pygame
import time
from pygame import mixer
pygame.init()
mixer.init()
class Player():
    def __init__(self):
        self.player_imgs=['graphics/Player/player_stand.png','graphics/Player/player_walk_1.png','graphics/Player/player_walk_2.png']
        self.player_img=pygame.image.load(self.player_imgs[0])
        self.clock=pygame.time.Clock()
        self.player_rect=self.player_img.get_rect()
        self.health=100
        self.velocity=8
        self.key=pygame.key.get_pressed()
        self.weight=10
        self.value=-1
        
        pygame.mixer.init()  # raises exception on fail

        # load the sound
        self.sound = pygame.mixer.Sound("audio/jump.mp3")
        self.sound.set_volume(0.2)

        # start playing
        print("Playing Sound...")
    def jump(self):
        #Play the music
        # self.sound.play()
        self.player_rect.top-=30
        if self.player_rect.top<100:
            self.player_rect.top+=10
    def player_walk(self):
        #  for i in range(3):
        #     value=i
        #     self.player_img=pygame.image.load(self.player_imgs[value])
        #     if value==2:
        #         value=0
        #     value+=1

        #     time.sleep(0.3)
        self.value+=1
        if self.value==3:
            self.value=0
        self.player_img=pygame.image.load(self.player_imgs[self.value])
        if self.player_rect.y<300-self.player_rect.height:
            self.player_img=pygame.image.load("graphics/Player/jump.png")




 

