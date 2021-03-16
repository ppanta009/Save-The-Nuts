"""config file"""
import os

'''THIS SECTION OF CODE STORES ALL THE IMAGES AND AUDIO FILES IN THE DICTIONARY AND
THE MAIN FUNCTION USES THESE DICTIONARY TO PUT IMAGES AND MUSIC IN GAME'''

# FRAMES PER SECOND
FPS = 50

# defining the screensize
SCREENSIZE = (640, 480)

# defining the image path and storing it in dictionary
IMAGE_PATHS = {
                'human': os.path.join(os.getcwd(), 'resources/images/dude.png'),
                'grass': os.path.join(os.getcwd(), 'resources/images/grass.png'),
                'nuts': os.path.join(os.getcwd(), 'resources/images/nuts.png'),
                'bullet': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
                'villain': os.path.join(os.getcwd(), 'resources/images/villain.png'),
                'healthbar': os.path.join(os.getcwd(), 'resources/images/healthbar.png'),
                'health': os.path.join(os.getcwd(), 'resources/images/health.png'),
                'gameover': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
                'youwin': os.path.join(os.getcwd(), 'resources/images/youwin.png')
            }
# defining the sound path and storing it in dictionary
SOUNDS_PATHS = {
                'hit': os.path.join(os.getcwd(), 'resources/audio/explode.wav'),
                'enemy': os.path.join(os.getcwd(), 'resources/audio/enemy.wav'),
                'shoot': os.path.join(os.getcwd(), 'resources/audio/shoot.wav'),
                'moonlight': os.path.join(os.getcwd(), 'resources/audio/moonlight.wav')
            }
