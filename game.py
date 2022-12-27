
import pygame
from sys import exit
pygame.init()
pygame.display.set_caption('Game')
FPS = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))
grass = pygame.image.load('imgonline-com-ua-BigPicture-VnIr9ErAPB.jpg')
unit = pygame.image.load('pngwing_com.X1CU5.png')
unit_x = 800
unit_y = 300
unit_hp = 4
unit_hp4 = pygame.image.load('free-png.ru-55.png')
unit_hp3 = pygame.image.load('heartlove-искусства-bit-пикселей-загрузка-изолированную-иллюстрацию-195804754.jpg')
unit_hp2 = pygame.image.load('np4.png')
unit_hp1 = pygame.image.load('56e3376efd62f68b12d3295d.jpg')
unit_hp0 = pygame.image.load('imgonline-com-ua-BigPicture-FYBvZrCBaHn.jpg')
while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
             pygame.quit()
             exit()
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_w:
                    unit_y -= 50

               if event.key == pygame.K_d:
                    unit_x += 200

               if event.key == pygame.K_a:
                    unit_x -= 200

               if event.key == pygame.K_s:
                    unit_y += 50

               if event.key == pygame.K_m:
                    pygame.quit()
                    exit()
          if event.type == pygame.MOUSEMOTION:
               print(event.pos)
     screen.blit(grass,(0,0))
     screen.blit(unit,(unit_x,unit_y))
     if unit_x > 1920:
          unit_x -= 1920
          unit_hp -= 1
     if unit_x < 0:
          unit_x += 1920
          unit_hp -= 1
     if unit_y < 0:
          unit_y += 1080
          unit_hp -= 1
     if unit_y > 1080:
          unit_y -= 1080
          unit_hp -= 1




     if unit_hp == 4:
          screen.blit(unit_hp4,(0,0))
     if unit_hp == 3:
          screen.blit(unit_hp3,(0,0))
     if unit_hp == 2:
          screen.blit(unit_hp2,(0,0))
     if unit_hp == 1:
          screen.blit(unit_hp1,(0,0))
     if unit_hp == 0:
          screen.blit(unit_hp0,(0,0))
     keys = pygame.key.get_pressed()
     pygame.display.update()
     FPS.tick(60)

