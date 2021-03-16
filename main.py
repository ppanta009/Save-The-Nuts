import cfg
import random
from modules.Sprites import *
from modules.interfaces import *

'''start the game '''


def initGame():

    # Initialize pygame, set the display window
    pygame.init()
    pygame.mixer.init()

    '''set the screen size and create the screen'''
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('Save the nut: Developed by Pravakar Panta')

    # load necessary game material i.e. images and sounds
    game_images = {}
    for key, value in cfg.IMAGE_PATHS.items():
        game_images[key] = pygame.image.load(value)
    game_sounds = {}

    # making sure that music played is not background track and act accordingly
    for key, value in cfg.SOUNDS_PATHS.items():
        if key != 'moonlight':
            game_sounds[key] = pygame.mixer.Sound(value)
    return screen, game_images, game_sounds


'''main function'''
def main():
    # initialization
    screen, game_images, game_sounds = initGame()

    # play background music
    pygame.mixer.music.load(cfg.SOUNDS_PATHS['moonlight'])
    pygame.mixer.music.play(-1, 0.0)

    # font loading
    font = pygame.font.Font(None, 24)

    # setting postion of human who is firing
    bunny = BunnySprite(image=game_images.get('human'), position=(100, 100))

    # Tracking the player's accuracy variable, the number of bullet shot and the number of badgers hit are recorded.
    acc_record = [0., 0.]

    # setting the life value
    healthvalue = 194

    # gun and bullet
    bullet_sprites_group = pygame.sprite.Group()

    # setting pos of squirrel and adding more squirrel
    villain_sprites_group = pygame.sprite.Group()
    villain = villainSprite(game_images.get('villain'), position=(640, 100))
    villain_sprites_group.add(villain)

    # timer is defined so new squirrel will be defined after a period of  time
    badtimer = 100
    badtimer1 = 0

    '''the running variable will track whether the game is over, 
        and the exitcode variable will track whether the player won. this all happens in main loop'''
    running, exitcode = True, False
    clock = pygame.time.Clock()
    while running:

        # --fill screen with black before drawing anything in the screen
        screen.fill(0)

        # --add scenery to the background
        for x in range(cfg.SCREENSIZE[0] // game_images['grass'].get_width() + 1):
            for y in range(cfg.SCREENSIZE[1] // game_images['grass'].get_height() + 1):
                screen.blit(game_images['grass'], (x * 100, y * 100))
        for i in range(4): screen.blit(game_images['nuts'], (0, 30 + 105 * i))

        # --countdown information
        countdown_text = font.render(str((90000 - pygame.time.get_ticks()) // 60000) + ":" + str(
            (90000 - pygame.time.get_ticks()) // 1000 % 60).zfill(2), True, (0, 0, 0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topright = [635, 5]  # showing location of countdown clock
        screen.blit(countdown_text, countdown_rect)

        '''detecting the button and getting out of the game. Also counting the accurate hits. 
        Also it determines the sound while shooting the bullet and the direction to rotate the 
        human when the mouse is moved and adding more bullets to shoot at the rabbit'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # getting out of pygame
                sys.exit()  # exiting the sys module
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_sounds['shoot'].play()  # setting sound while shooting the bullet
                acc_record[1] += 1  # counting accurate hits
                mouse_pos = pygame.mouse.get_pos()  # setting position of mouse
                angle = math.atan2(mouse_pos[1] - (bunny.rotated_position[1] + 32),
                                   mouse_pos[0] - (bunny.rotated_position[0] + 26))  # direction to rotate human
                bullet = bulletSprite(game_images.get('bullet'),
                                      (angle, bunny.rotated_position[0] + 32, bunny.rotated_position[1] + 26))
                bullet_sprites_group.add(bullet)  # add more bullets

        # ---move the human
        # ---following line of code moves human when pressed designated key
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            bunny.move(cfg.SCREENSIZE, 'up')
        elif key_pressed[pygame.K_s]:
            bunny.move(cfg.SCREENSIZE, 'down')
        elif key_pressed[pygame.K_a]:
            bunny.move(cfg.SCREENSIZE, 'left')
        elif key_pressed[pygame.K_d]:
            bunny.move(cfg.SCREENSIZE, 'right')

        # update gun and bullet
        for bullet in bullet_sprites_group:
            if bullet.update(cfg.SCREENSIZE):
                bullet_sprites_group.remove(bullet)

        # following line of codes will update the squirrel and send them from random position
        if badtimer == 0:
            villain = villainSprite(game_images.get('villain'), position=(640, random.randint(50, 430)))
            villain_sprites_group.add(villain)
            badtimer = 100 - (badtimer1 * 2)
            badtimer1 = 20 if badtimer1 >= 20 else badtimer1 + 2
        badtimer -= 1

        '''  following line of code will determine the reduction in health value randomly 
        and removes the the villains that have been hit '''
        for villain in villain_sprites_group:
            if villain.update():
                game_sounds['hit'].play()
                healthvalue -= random.randint(4, 8)
                villain_sprites_group.remove(villain)

        # --checking the impact of the hit
        for bullet in bullet_sprites_group:
            for villain in villain_sprites_group:
                if pygame.sprite.collide_mask(bullet, villain):
                    game_sounds['enemy'].play()
                    bullet_sprites_group.remove(bullet)
                    villain_sprites_group.remove(villain)
                    acc_record[0] += 1

        # draw gun and bullet
        bullet_sprites_group.draw(screen)

        # draw squirrel
        villain_sprites_group.draw(screen)

        # draw human
        bunny.draw(screen, pygame.mouse.get_pos())

        # draw the health , draw red health bar first then add green to the health bar
        screen.blit(game_images.get('healthbar'), (5, 5))
        for i in range(healthvalue):
            screen.blit(game_images.get('health'), (i + 8, 8))

        # determine if the game is over
        if pygame.time.get_ticks() >= 90000:
            running, exitcode = False, True
        if healthvalue <= 0:
            running, exitcode = False, False

        # update screen
        pygame.display.flip()
        clock.tick(cfg.FPS)

    # calculation accuracy
    accuracy = acc_record[0] / acc_record[1] * 100 if acc_record[1] > 0 else 0
    accuracy = '%.2f' % accuracy
    showEndGameInterface(screen, exitcode, accuracy, game_images)


'''run the game'''
if __name__ == '__main__':
    main()
