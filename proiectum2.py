import pygame


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
difficulty=None

def player(player_x, player_y):
    screen.blit(player_black, (player_x, player_y))

def method2():
    global difficulty
    global running
    pos = None

    while running:

        screen.fill((120, 24, 130))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # checking pressed keys
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                player(pos[0], pos[1])
                if 0<(pos[0]-250)/400<1 and 0<(pos[1]-200)/80<1:
                    difficulty=1
                    running=False
                    print("beginner")
                if 0<(pos[0]-250)/400<1 and 0<(pos[1]-400)/80<1:
                    difficulty=3
                    running=False
                    print("Medium")
                if 0<(pos[0]-250)/400<1 and 0<(pos[1]-600)/80<1:
                    difficulty=5
                    running=False
                    print("Advanced")
        pygame.draw.rect(screen,(48, 25, 52),pygame.Rect(250, 200, 400, 80))
        pygame.draw.rect(screen, (48, 25, 70), pygame.Rect(250, 400, 400, 80))
        pygame.draw.rect(screen, (48, 25, 90), pygame.Rect(250, 600, 400, 80))
        font=pygame.font.Font(pygame.font.get_default_font(), 44)
        text=font.render("Begginer",True,(0, 0, 0))
        text_rect = text.get_rect()
        screen.blit(text,((900-text_rect.width)/2,200+text_rect.height/2))
        font=pygame.font.Font(pygame.font.get_default_font(), 44)
        text=font.render("Medium",True,(0, 0, 0))
        text_rect = text.get_rect()
        screen.blit(text,((900-text_rect.width)/2,400+text_rect.height/2))
        font = pygame.font.Font(pygame.font.get_default_font(), 44)
        text = font.render("Advanced", True, (0, 0, 0))
        text_rect = text.get_rect()
        screen.blit(text, ((900 - text_rect.width) / 2, 600 + text_rect.height / 2))
        pygame.display.update()

    return difficulty
