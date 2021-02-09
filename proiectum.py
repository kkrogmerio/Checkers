import pygame
from proiectum2 import *

pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Checkers")
running = True
icon = pygame.image.load("checkers_PNG40.png")
player_black = pygame.image.load("black.png")
player_black_x = 100
player_black_y = 100
player_black_king = pygame.image.load("black_king.png")
player_white = pygame.image.load("white.png")
player_white_king = pygame.image.load("white_king.png")
pygame.display.set_icon(icon)
pos = None


def player(player_x, player_y):
    screen.blit(player_black, (player_x, player_y))
player=None

pos = None
def method1():
    global player
    global running
    print("INTRADDDDDDI")
    while running:

        screen.fill((120, 24, 74))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # checking pressed keys
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 0 < (pos[0] - 250) / 400 < 1 and 0 < (pos[1] - 300) / 100 < 1:
                    player='a'
                    print("White chosen")
                    running=False
                    break
                if 0 < (pos[0] - 250) / 400 < 1 and 0 < (pos[1] - 500) / 100 < 1:
                    player='b'
                    print("Black chosen")
                    running=False
                    break
        pygame.draw.rect(screen,(48, 25, 52),pygame.Rect(250, 300, 400, 100))
        pygame.draw.rect(screen, (48, 25, 52), pygame.Rect(250, 500, 400, 100))
        font=pygame.font.Font(pygame.font.get_default_font(), 44)
        text=font.render("Choose white",True,(255, 255, 255))
        text_rect = text.get_rect()
        screen.blit(text,((900-text_rect.width)/2,300+text_rect.height/2))
        font=pygame.font.Font(pygame.font.get_default_font(), 44)
        text=font.render("Choose black",True,(0, 0, 0))
        text_rect = text.get_rect()
        screen.blit(text,((900-text_rect.width)/2,500+text_rect.height/2))
        pygame.display.update()

    return player

