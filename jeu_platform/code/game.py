import pygame
from pygame import mixer
import sys
import random
from player import Player
from snail import Snail
from bird import Bird
from button import Button
pygame.init()
mixer.init()

class Game():      
    def __init__(self):
        self.window=pygame.display.set_mode((800,400))
        self.window_title=pygame.display.set_caption("Ceph_game_2d")
        self.clock=pygame.time.Clock()
        self.player=Player()
        self.player.player_rect.x=50

        self.snail=Snail()
        self.snail.rect.x=700
        self.snail.rect.top=300-self.snail.rect.height
        self.snail2=Snail()
        self.snail2.rect.x=3000
        self.snail2.rect.top=300-self.snail.rect.height

        self.bird=Bird()
        self.bird.rect.top=70
        self.bird.rect.x=2000

        self.index=0
        self.pressed={}
        self.is_open=True

        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.black = (0, 0, 0)
        self.lose_font=pygame.font.Font("font/Pixeltype.ttf",32)
        self.lose_text=self.lose_font.render("""Game   over  """"push   R   to   restart",True,self.green,self.blue)
        
        self.execute=True

        font = pygame.font.Font(None, 25)

        self.frame_count = 0
        self.frame_rate = 60
        self.start_time = 90
        #Instantiate mixer
        mixer.init()

        #Load audio file
        mixer.music.load('audio/music.wav')

        print("music started playing....")

        #Set preferred volume
        mixer.music.set_volume(0.2)

        #Play the music
        mixer.music.play()

    def decor(self):
        self.sky_img=pygame.image.load("graphics/Sky.png")
        self.ground_img=pygame.image.load("graphics/ground.png")
        self.sky_rect=self.ground_img.get_rect()
        self.ground_rect=self.ground_img.get_rect()
        self.ground_rect.y+=300   
        return self.window.blit(self.sky_img,self.sky_rect),self.window.blit(self.ground_img,self.ground_rect)
    
    def game_system(self):
        while self.is_open:
            # if self.game_status=="game_menu":

                self.decor()
                self.window.blit(self.player.player_img,self.player.player_rect)
                self.window.blit(self.snail.img,self.snail.rect)
                self.window.blit(self.snail2.img,self.snail2.rect)

                self.window.blit(self.bird.img,self.bird.rect)

                # self.optional_snail2_x-=6
                self.random=random.randint(0,10)
            
                if self.player.player_rect.top!=300-self.player.player_rect.height and not self.ground_rect.colliderect(self.player.player_rect) :
                    self.player.player_rect.top+=self.player.weight
                if self.execute:
                    self.snail.forward(800)
                    self.snail2.forward(2500)
                    self.snail.snail_walk()
                    self.bird.forward()
                if self.snail.rect.colliderect(self.player.player_rect) or self.snail2.rect.colliderect(self.player.player_rect):
                    self.snail.rect.x=self.player.player_rect.x+self.snail.rect.width
                    self.execute=False
                if self.bird.rect.colliderect(self.player.player_rect):
                    self.bird.rect.x=self.player.player_rect.x+self.bird.rect.width-10
                    self.execute=False
                    # print("mort")
            
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        self.is_open=False
                        pygame.quit()
                        sys.exit()
                    elif event.type==pygame.KEYDOWN:
                        self.pressed[event.key]=True
                        if event.key==pygame.K_SPACE:
                            self.player.sound.play() 
                        elif event.key==pygame.K_r and self.execute==False:
                            self.execute=True                   
                            self.snail.rect.x=700
                            print("r")
    
                    elif event.type==pygame.KEYUP:
                        self.pressed[event.key]=False
                        
                if self.pressed.get(pygame.K_SPACE) and self.execute:
                    self.player.jump()
                if self.execute:
                    self.player.player_walk()
                if self.execute==False:
                    self.window.fill((25,0,100))
                    self.window.blit(self.lose_text,(800/2-125,300/2))

                    # self.window.blit(self.buttonSurface, self.buttonRect)

                # timer section
                    # --- Timer going up ---
                # Calculate total seconds
                total_seconds = self.frame_count // self.frame_rate

                # Divide by 60 to get total minutes
                minutes = total_seconds // 60

                # Use modulus (remainder) to get seconds
                seconds = total_seconds % 60

                # Use python string formatting to format in leading zeros
                output_string = "score: {0:02}:{1:02}".format(minutes, seconds)

                # Blit to the screen
                text = self.lose_font.render(output_string, True,self.white )
                self.window.blit(text, (800/2-50, 50))

    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
                total_seconds = self.start_time - (self.frame_count // self.frame_rate)
                if total_seconds < 0:
                    total_seconds = 0

    # Divide by 60 to get total minutes
                minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
                seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    # Blit to the screen
                self.text = self.lose_font.render(output_string, True, self.black)
                
                if self.execute==True:

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
                    self.frame_count += 1





                
                pygame.display.flip()
        
                self.clock.tick(30)

    def run(self):
            self.game_system()
            print(self.game_status)

j=Game()
j.run()