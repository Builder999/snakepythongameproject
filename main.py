import pygame
import random
dis_width = 480
dis_height = 480
screen = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("SNEK")
done = False
changex = 0
changey = 0


class snake:
    x = 10
    y = 10
    length = 1
    speed = 10
    snake = pygame.Rect(x,y,10,10)
    direction = 0
    snakeHead = []
    snakeList = []
    def update(self):
        if (self.direction == 0):
            self.x = self.x + self.speed
        elif (self.direction == 1):
            self.x = self.x - self.speed
        elif (self.direction == 2):
            self.y = self.y - self.speed
        elif (self.direction == 3):
            self.y = self.y + self.speed
        
        if len(self.snakeList) > self.length:
            del self.snakeList[0]
        for x in self.snakeList:
        
            self.snake = pygame.Rect(x[0],x[1],10,10)    
            pygame.draw.rect(screen, (0,128,255), self.snake)
        self.snakeHead = []
        self.snakeHead.append(self.x)
        self.snakeHead.append(self.y)
        
        #if self.snakeHead in self.snakeList[:-1]:
        #    global done 
        #    done = True
        
        self.snakeList.append(self.snakeHead)
    def isCollided(self):
        for x in self.snakeList[:-1]:
            if x == self.snakeHead:
                return True
            


class food:
    x = random.randrange(10,480,10)
    y = random.randrange(10,480,10)
    food = pygame.Rect(x,y,10,10)
    def update(self):
        pygame.draw.rect(screen, (255,255,255), self.food)
    def move(self):
        print("doing")
        self.x = random.randrange(10,480,10)
        self.y = random.randrange(10,480,10)
        self.food = pygame.Rect(self.x,self.y,10,10)
Snake = snake()
Food = food()
pygame.key.set_repeat(0,0)
while not done:
    FPS = pygame.time.Clock()
    FPS.tick(15)
    screen.fill((0,0,0))
    # event grabber
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #rectangle draw

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        Snake.direction = 2
    if pressed[pygame.K_DOWN]:
        Snake.direction = 3
    if pressed[pygame.K_LEFT]:
        Snake.direction = 1
    if pressed[pygame.K_RIGHT]:
        Snake.direction = 0
    if Snake.x > dis_width or Snake.x < 0 or Snake.y > dis_height or Snake.y < 0:
        done = True
    if Snake.isCollided():
        done = True
    Food.update()
    Snake.update()

    if Snake.x == Food.x and Snake.y == Food.y:
        Food.move()
        Snake.length += 1
    pygame.display.flip()
