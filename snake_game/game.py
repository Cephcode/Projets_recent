# import
import pygame
import random
from sys import exit
from food import Food
from snake import Snake

# init
pygame.init()
# variable
Nb_col=10
Nb_Row=15
Cell_size=40

window=pygame.display.set_mode(size=(Nb_col*Cell_size,Nb_Row*Cell_size))
running=True
clock=pygame.time.Clock()

font=pygame.font.Font("3AB0DB_3_0.ca19d9b3.ttf",32)
# font.render("hello",True,pygame.Color("green"),pygame.Color("black"))

# timer
screen_update=pygame.USEREVENT
pygame.time.set_timer(screen_update,200)
# # personnage
# food=Food(window,Cell_size,Nb_col,Nb_Row)
# snake=Snake(window,Cell_size)

def show_grid():
    for i in range(0,Nb_col):
        for j in range(0,Nb_Row):
            rect=pygame.Rect(i*Cell_size,j*Cell_size,Cell_size,Cell_size)
            pygame.draw.rect(window,pygame.Color("black"),rect,1)
class Game():
    def __init__(self):
    # personnage
        self.food=Food(window,Cell_size,Nb_col,Nb_Row)
        self. snake=Snake(window,Cell_size)
        self.generate_food()
    def update(self):
            self.snake.move_snake()
            self.collide()
            self.game_over()

                
    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()
    def collide(self):
        snake_length=len(self.snake.body)
        snake_head_block=self.snake.body[snake_length-1]
        food_block=self.food.block
        if snake_head_block.x==food_block.x and snake_head_block.y==food_block.y:
            self.generate_food()
        else:
            self.snake.body.pop(0)
        
    def game_over(self):
        snake_length=len(self.snake.body)
        snake_head=self.snake.body[snake_length-1]
        if snake_head.x not in range(0,Nb_col) or snake_head.y not in range(0,Nb_Row):
            print("game_over")
            # font.render("hello",pygame.Color("green"),pygame.Color("black"))
            pygame.quit()
            exit()
        for block in self.snake.body[0:snake_length-1]:
            if block.x==snake_head.x and block.y==snake_head.y:
                print("game_over")
                # font.render("hello",pygame.Color("green"),pygame.Color("black"))
                pygame.quit()
                exit()




    def generate_food(self):
        self.food=Food(window,Cell_size,Nb_col,Nb_Row)
        should_generate=True
        while should_generate:
            count=0
            for block in self.snake.body:
                if block.x==self.food.block.x and block.y==self.food.block.y: 
                    count+=1
                if count==0:
                    should_generate=False
                else:
                    self.food=Food(window,Cell_size,Nb_col,Nb_Row)     
game=Game()
# def collide 
# boucle principal
while running:
    window
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                game.snake.direction="right"
            elif event.key==pygame.K_LEFT:
                game.snake.direction="left"
            elif event.key==pygame.K_UP:
                game.snake.direction="top"
            elif event.key==pygame.K_DOWN:
                game.snake.direction="down"
        elif event.type==screen_update:
            game.update()
    window.fill(pygame.Color("white"))
    show_grid()

    game.draw_elements()

    pygame.display.flip()
    clock.tick(60)
        