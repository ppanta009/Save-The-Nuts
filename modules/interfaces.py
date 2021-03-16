
import sys
import pygame


'''THIS SECTION OF CODE IS TO DEFINE THE INTERFACE WHEN THE GAME IS OVER'''


def showEndGameInterface(screen, exitcode, accuracy, game_images):
    """ DETERMINES THE FONT OF THE TXT AND ITS COLOR AS WELL"""
    font = pygame.font.Font(None, 44)
    text = font.render(f"Accuracy: {accuracy}%", True, (255, 0, 0))
    text_rect = text.get_rect()

    '''SET THE LOCATION OF THE TEXT THAT SHOWS ACCURACT '''
    text_rect.centerx = screen.get_rect().centerx + 180
    text_rect.centery = screen.get_rect().centery + 180
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if exitcode:
            screen.blit(game_images['youwin'], (0, 0))
        else:
            screen.blit(game_images['gameover'], (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
