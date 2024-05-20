print("LOADING...")

# Imports
import pygame
import entities_v4 as entities


# Screen settings

SCALE = 70 # SCALE is short for Scale Factor. SCALE is the size of one square.
WIDTH = 14 * SCALE
HEIGHT = 14 * SCALE
TITLE = "Escape from the Tower of Treasure!"
FPS = 60


# Initialize game engine
pygame.init()
show_start_screen_again = True


# Make the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 225, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BROWN = (89, 53, 29)
COLOR_BG = (BROWN)


# Image Functions
'''Items and the like'''
def upload_jasper_icon():
    screen.blit(jasper_icon_img, [0, 0])

def upload_a_coin():
    screen.blit(a_coin_img, [0, 0])

def upload_five_coin():
    screen.blit(five_coin_img, [0, 0])

def upload_ten_emerald():
    screen.blit(ten_emerald_screen_img, [0, 0])

def upload_fifteen_diamond():
    screen.blit(fifteen_diamond_img, [0, 0])

def upload_goal():
    screen.blit(goal_img, [0, 0])

def upload_floor_1_goal():
    screen.blit(goal_img, [0, 0])

'''Screens'''
def upload_start_screen():
    screen.blit(start_screen_img, [0, 0])

def upload_lose_screen():
    screen.blit(lose_screen_img, [0, 0])

def upload_try_again_screen():
    screen.blit(try_again_screen_img, [0, 0])

def upload_nice_work_screen():
    screen.blit(nice_work_screen_img, [0, 0])

def upload_winner_screen():
    screen.blit(winner_screen_img, [0, 0])

'''Cutscenes'''
def upload_cutscene_1():
    screen.blit(cutscene_1_img, [0, 0])

def upload_cutscene_2():
    screen.blit(cutscene_2_img, [0, 0])

def upload_cutscene_3():
    screen.blit(cutscene_3_img, [0, 0])

def upload_cutscene_4():
    screen.blit(cutscene_4_img, [0, 0])

def upload_cutscene_5():
    screen.blit(cutscene_5_img, [0, 0])

def upload_cutscene_6():
    screen.blit(cutscene_6_img, [0, 0])

def upload_cutscene_7():
    screen.blit(cutscene_7_img, [0, 0])

def upload_cutscene_8():
    screen.blit(cutscene_8_img, [0, 0])

def upload_cutscene_9():
    screen.blit(cutscene_9_img, [0, 0])

def upload_cutscene_10():
    screen.blit(cutscene_10_img, [0, 0])

def upload_cutscene_instruct():
    screen.blit(cutscene_instruct_img, [0, 0])

# Sound Functions
def play_lose():
    lose_sfx.play()

def play_try_again():
    try_again_sfx.play()

def play_nice_work():
    nice_work_sfx.play()
    
def play_winner():
    winner_sfx.play()

# Fonts
FONT_SM = pygame.font.Font('fonts/mario_word.ttf', int(SCALE // 2.5))
FONT_MD = pygame.font.Font('fonts/mario_word.ttf', int(SCALE // 1.5))
FONT_LG = pygame.font.Font('fonts/mario_word.ttf', int(SCALE * 1.75))
FONT_TITLE = pygame.font.Font('fonts/mario_word.ttf', int(SCALE))
FONT_EXIT_TOWER = pygame.font.Font('fonts/mario_word.ttf', int(SCALE // 1.6))
FONT_FINAL_SCORE = pygame.font.Font('fonts/mario_word.ttf', int(SCALE // 1.1))

# Images
'''Items and the like'''
jasper_icon_img = pygame.image.load('Images/jasper_icon.png').convert_alpha()
jasper_icon_img = pygame.transform.scale_by(jasper_icon_img, [SCALE / 100, SCALE / 100])

a_coin_img = pygame.image.load('Images/a_coin.png').convert_alpha()
a_coin_img = pygame.transform.scale_by(a_coin_img, [SCALE / 100, SCALE / 100])

five_coin_img = pygame.image.load('Images/five_coin.png').convert_alpha()
five_coin_img = pygame.transform.scale_by(five_coin_img, [SCALE / 100, SCALE / 100])

ten_emerald_img = pygame.image.load('Images/ten_emerald.png').convert_alpha()
ten_emerald_img = pygame.transform.scale_by(ten_emerald_img, [SCALE / 100, SCALE / 100])

fifteen_diamond_img = pygame.image.load('Images/fifteen_diamond.png').convert_alpha()
fifteen_diamond_img = pygame.transform.scale_by(fifteen_diamond_img, [SCALE / 100, SCALE / 100])

goal_img = pygame.image.load('Images/goal.png').convert_alpha()
goal_img = pygame.transform.scale_by(goal_img, [SCALE / 100, SCALE / 100])

floor_1_goal_img = pygame.image.load('Images/floor_1_goal.png').convert_alpha()
floor_1_goal_img = pygame.transform.scale_by(floor_1_goal_img, [SCALE / 100, SCALE / 100])

'''Screens'''
start_screen_img = pygame.image.load('Images/start_screen.png').convert_alpha()
start_screen_img = pygame.transform.scale_by(start_screen_img, [SCALE / 50, SCALE / 50])

lose_screen_img = pygame.image.load('Images/lose_screen.png').convert_alpha()
lose_screen_img = pygame.transform.scale_by(lose_screen_img, [SCALE / 50, SCALE / 50])

try_again_screen_img = pygame.image.load('Images/try_again_screen.png').convert_alpha()
try_again_screen_img = pygame.transform.scale_by(try_again_screen_img, [SCALE / 50, SCALE / 50])

nice_work_screen_img = pygame.image.load('Images/nice_work_screen.png').convert_alpha()
nice_work_screen_img = pygame.transform.scale_by(nice_work_screen_img, [SCALE / 50, SCALE / 50])

winner_screen_img = pygame.image.load('Images/winner_screen.png').convert_alpha()
winner_screen_img = pygame.transform.scale_by(winner_screen_img, [SCALE / 50, SCALE / 50])

'''Cutscenes'''
cutscene_1_img = pygame.image.load('Images/cutscene_1.png').convert_alpha()
cutscene_1_img = pygame.transform.scale_by(cutscene_1_img, [SCALE / 50, SCALE / 50])

cutscene_2_img = pygame.image.load('Images/cutscene_2.png').convert_alpha()
cutscene_2_img = pygame.transform.scale_by(cutscene_2_img, [SCALE / 50, SCALE / 50])

cutscene_3_img = pygame.image.load('Images/cutscene_3.png').convert_alpha()
cutscene_3_img = pygame.transform.scale_by(cutscene_3_img, [SCALE / 50, SCALE / 50])

cutscene_4_img = pygame.image.load('Images/cutscene_4.png').convert_alpha()
cutscene_4_img = pygame.transform.scale_by(cutscene_4_img, [SCALE / 50, SCALE / 50])

cutscene_5_img = pygame.image.load('Images/cutscene_5.png').convert_alpha()
cutscene_5_img = pygame.transform.scale_by(cutscene_5_img, [SCALE / 50, SCALE / 50])

cutscene_6_img = pygame.image.load('Images/cutscene_6.png').convert_alpha()
cutscene_6_img = pygame.transform.scale_by(cutscene_6_img, [SCALE / 50, SCALE / 50])

cutscene_7_img = pygame.image.load('Images/cutscene_7.png').convert_alpha()
cutscene_7_img = pygame.transform.scale_by(cutscene_7_img, [SCALE / 50, SCALE / 50])

cutscene_8_img = pygame.image.load('Images/cutscene_8.png').convert_alpha()
cutscene_8_img = pygame.transform.scale_by(cutscene_8_img, [SCALE / 50, SCALE / 50])

cutscene_9_img = pygame.image.load('Images/cutscene_9.png').convert_alpha()
cutscene_9_img = pygame.transform.scale_by(cutscene_9_img, [SCALE / 50, SCALE / 50])

cutscene_10_img = pygame.image.load('Images/cutscene_10.png').convert_alpha()
cutscene_10_img = pygame.transform.scale_by(cutscene_10_img, [SCALE / 50, SCALE / 50])

cutscene_instruct_img = pygame.image.load('Images/cutscene_instruct.png').convert_alpha()
cutscene_instruct_img = pygame.transform.scale_by(cutscene_instruct_img, [SCALE / 50, SCALE / 50])

# Sound Effects (SFX)
lose_sfx = pygame.mixer.Sound('SFX/lose.mp3')

try_again_sfx = pygame.mixer.Sound('SFX/try_again.mp3')

nice_work_sfx = pygame.mixer.Sound('SFX/nice_work.mp3')

winner_sfx = pygame.mixer.Sound('SFX/winner.mp3')

# Background Music
time_mine_mus = 'Music/fuzzy_time_mine.mp3'

def play_fuzzy_time_mine():
    pygame.mixer.music.load(time_mine_mus)
    pygame.mixer.music.play(-1)


# Game Scenes
LOSE = -1
START = 0
CUTSCENE = 10
CUTSCENE_END = 20
PLAYING = 1
LEVEL_TRANSITION = 2
WIN_GAME = 3


# Helper Functions
def new_game():
    global p1, players, walls, items, coins, goals, current_scene, floor
    
    # Game Objects
    '''Player(s)'''
    p1 = entities.Player([6.25 * SCALE, 5 * SCALE], jasper_icon_img)

    players = pygame.sprite.Group()
    players.add(p1)
    
    floor = 10
    
    start_a_level()

def start_a_level():
    global p1, players, walls, items, coins, goals, current_scene, floor
    
        # FLOOR 10
    '''Horizontal Walls'''
    w0_1 = entities.Wall([5 * SCALE, 11 * SCALE], [SCALE * 4, SCALE], GRAY)
    '''Vertical Walls'''
    w0_2 = entities.Wall([5 * SCALE, 8 * SCALE], [SCALE, SCALE * 4], GRAY)
    w0_3 = entities.Wall([8 * SCALE, 8 * SCALE], [SCALE, SCALE * 4], GRAY)

        # FLOOR 9
    '''Horizontal Walls'''
    w1_1 = entities.Wall([2 * SCALE, 2 * SCALE], [SCALE * 4, SCALE], GRAY)
    w1_2 = entities.Wall([8 * SCALE, 2 * SCALE], [SCALE * 4, SCALE], GRAY)
    w1_3 = entities.Wall([5 * SCALE, 5 * SCALE], [SCALE * 7, SCALE], GRAY)
    w1_4 = entities.Wall([11 * SCALE, 8 * SCALE], [SCALE * 3, SCALE], GRAY)
    w1_5 = entities.Wall([2 * SCALE, 11 * SCALE], [SCALE * 7, SCALE], GRAY)
    '''Vertical Walls'''
    w1_6 = entities.Wall([8 * SCALE, 0], [SCALE, SCALE * 3], GRAY)
    w1_7 = entities.Wall([5 * SCALE, 2 * SCALE], [SCALE, SCALE * 7], GRAY)
    w1_8 = entities.Wall([2 * SCALE, 5 * SCALE], [SCALE, SCALE * 7], GRAY)
    w1_9 = entities.Wall([11 * SCALE, 5 * SCALE], [SCALE, SCALE * 7], GRAY)
    w1_10 = entities.Wall([8 * SCALE, 8 * SCALE], [SCALE, SCALE * 6], GRAY)

        # FLOOR 8
    '''Horizontal Walls'''
    w2_1 = entities.Wall([0, 2 * SCALE], [12 * SCALE, SCALE], GRAY)
    w2_2 = entities.Wall([5 * SCALE, 5 * SCALE], [9 * SCALE, SCALE], GRAY)
    w2_3 = entities.Wall([8 * SCALE, 8 * SCALE], [6 * SCALE, SCALE], GRAY)
    w2_4 = entities.Wall([2 * SCALE, 11 * SCALE], [4 * SCALE, SCALE], GRAY)
    w2_5 = entities.Wall([8 * SCALE, 11 * SCALE], [4 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w2_6 = entities.Wall([2 * SCALE, 5 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w2_7 = entities.Wall([5 * SCALE, 5 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w2_8 = entities.Wall([8 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)

        # FLOOR 7
    '''Horizontal Walls'''
    w3_1 = entities.Wall([0, 2 * SCALE], [3 * SCALE, SCALE], GRAY)
    w3_2 = entities.Wall([8 * SCALE, 2 * SCALE], [3 * SCALE, SCALE], GRAY)
    w3_3 = entities.Wall([2 * SCALE, 5 * SCALE], [4 * SCALE, SCALE], GRAY)
    w3_4 = entities.Wall([8 * SCALE, 5 * SCALE], [6 * SCALE, SCALE], GRAY)
    w3_5 = entities.Wall([2 * SCALE, 8 * SCALE], [7 * SCALE, SCALE], GRAY)
    w3_6 = entities.Wall([5 * SCALE, 11 * SCALE], [7 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w3_7 = entities.Wall([5 * SCALE, 0], [SCALE, 6 * SCALE], GRAY)
    w3_8 = entities.Wall([8 * SCALE, 2 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w3_9 = entities.Wall([2 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w3_10 = entities.Wall([11 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w3_11 = entities.Wall([5 * SCALE, 11 * SCALE], [SCALE, 3 * SCALE], GRAY)

        # FLOOR 6
    '''Horizontal Walls'''
    w4_1 = entities.Wall([2 * SCALE, 2 * SCALE], [7 * SCALE, SCALE], GRAY)
    w4_2 = entities.Wall([2 * SCALE, 5 * SCALE], [4 * SCALE, SCALE], GRAY)
    w4_3 = entities.Wall([8 * SCALE, 5 * SCALE], [6 * SCALE, SCALE], GRAY)
    w4_4 = entities.Wall([5 * SCALE, 8 * SCALE], [7 * SCALE, SCALE], GRAY)
    w4_5 = entities.Wall([2 * SCALE, 11 * SCALE], [12 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w4_6 = entities.Wall([11 * SCALE, 0], [SCALE, 3 * SCALE], GRAY)
    w4_7 = entities.Wall([8 * SCALE, 2 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w4_8 = entities.Wall([2 * SCALE, 5 * SCALE], [SCALE, 7 * SCALE], GRAY)

        # FLOOR 5
    '''Horizontal Walls'''
    w5_1 = entities.Wall([2 * SCALE, 2 * SCALE], [4 * SCALE, SCALE], GRAY)
    w5_2 = entities.Wall([11 * SCALE, 2 * SCALE], [3 * SCALE, SCALE], GRAY)
    w5_3 = entities.Wall([8 * SCALE, 5 * SCALE], [4 * SCALE, SCALE], GRAY)
    w5_4 = entities.Wall([11 * SCALE, 8 * SCALE], [3 * SCALE, SCALE], GRAY)
    w5_5 = entities.Wall([0, 11 * SCALE], [3 * SCALE, SCALE], GRAY)
    w5_6 = entities.Wall([5 * SCALE, 11 * SCALE], [7 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w5_7 = entities.Wall([8 * SCALE, 0], [SCALE, 12 * SCALE], GRAY)
    w5_8 = entities.Wall([2 * SCALE, 2 * SCALE], [SCALE, 10 * SCALE], GRAY)
    w5_9 = entities.Wall([5 * SCALE, 2 * SCALE], [SCALE, 7 * SCALE], GRAY)

        # FLOOR 4
    '''Horizontal Walls'''
    w6_1 = entities.Wall([8 * SCALE, 2 * SCALE], [4 * SCALE, SCALE], GRAY)
    w6_2 = entities.Wall([5 * SCALE, 8 * SCALE], [7 * SCALE, SCALE], GRAY)
    w6_3 = entities.Wall([2 * SCALE, 11 * SCALE], [7 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w6_4 = entities.Wall([5 * SCALE, 0], [SCALE, 6 * SCALE], GRAY)
    w6_5 = entities.Wall([2 * SCALE, 2 * SCALE], [SCALE, 10 * SCALE], GRAY)
    w6_6 = entities.Wall([8 * SCALE, 2 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w6_7 = entities.Wall([11 * SCALE, 2 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w6_8 = entities.Wall([5 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w6_9 = entities.Wall([11 * SCALE, 8 * SCALE], [SCALE, 6 * SCALE], GRAY)

        # FLOOR 3
    '''Horizontal Walls'''
    w7_1 = entities.Wall([0, 2 * SCALE], [3 * SCALE, SCALE], GRAY)
    w7_2 = entities.Wall([8 * SCALE, 2 * SCALE], [6 * SCALE, SCALE], GRAY)
    w7_3 = entities.Wall([2 * SCALE, 5 * SCALE], [10 * SCALE, SCALE], GRAY)
    w7_4 = entities.Wall([5 * SCALE, 8 * SCALE], [4 * SCALE, SCALE], GRAY)
    w7_5 = entities.Wall([2 * SCALE, 11 * SCALE], [4 * SCALE, SCALE], GRAY)
    w7_6 = entities.Wall([8 * SCALE, 11 * SCALE], [6 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w7_7 = entities.Wall([5 * SCALE, 2 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w7_8 = entities.Wall([11 * SCALE, 2 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w7_9 = entities.Wall([2 * SCALE, 5 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w7_10 = entities.Wall([8 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)


        # FLOOR 2
    '''Horizontal Walls'''
    w8_1 = entities.Wall([5 * SCALE, 2 * SCALE], [9 * SCALE, SCALE], GRAY)
    w8_2 = entities.Wall([5 * SCALE, 5 * SCALE], [7 * SCALE, SCALE], GRAY)
    w8_3 = entities.Wall([0, 8 * SCALE], [3 * SCALE, SCALE], GRAY)
    w8_4 = entities.Wall([5 * SCALE, 8 * SCALE], [7 * SCALE, SCALE], GRAY)
    w8_5 = entities.Wall([0 * SCALE, 11 * SCALE], [6 * SCALE, SCALE], GRAY)
    w8_6 = entities.Wall([11 * SCALE, 11 * SCALE], [3 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w8_7 = entities.Wall([2 * SCALE, 2 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w8_8 = entities.Wall([11 * SCALE, 5 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w8_9 = entities.Wall([5 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w8_10 = entities.Wall([8 * SCALE, 8 * SCALE], [SCALE, 4 * SCALE], GRAY)

        # FLOOR 1
    '''Horizontal Walls'''
    w9_1 = entities.Wall([2 * SCALE, 2 * SCALE], [4 * SCALE, SCALE], GRAY)
    w9_2 = entities.Wall([8 * SCALE, 2 * SCALE], [4 * SCALE, SCALE], GRAY)
    w9_3 = entities.Wall([2 * SCALE, 8 * SCALE], [7 * SCALE, SCALE], GRAY)
    w9_4 = entities.Wall([11 * SCALE, 8 * SCALE], [3 * SCALE, SCALE], GRAY)
    w9_5 = entities.Wall([5 * SCALE, 11 * SCALE], [7 * SCALE, SCALE], GRAY)
    '''Vertical Walls'''
    w9_6 = entities.Wall([5 * SCALE, 0], [SCALE, 6 * SCALE], GRAY)
    w9_7 = entities.Wall([8 * SCALE, 2 * SCALE], [SCALE, 10 * SCALE], GRAY)
    w9_8 = entities.Wall([2 * SCALE, 5 * SCALE], [SCALE, 7 * SCALE], GRAY)
    w9_9 = entities.Wall([11 * SCALE, 5 * SCALE], [SCALE, 4 * SCALE], GRAY)
    w9_10 = entities.Wall([5 * SCALE, 11 * SCALE], [SCALE, 3 * SCALE], GRAY)
    
    walls = pygame.sprite.Group()


        # Items
    C_WIDTH = SCALE // 2
    C_HEIGHT = SCALE // 1.5

        # FLOOR 9 COINS
    '''$15'''
    fifteen_diamond_9_1 = entities.Item([12.25 * SCALE, 10 * SCALE], fifteen_diamond_img, 15)
    fifteen_diamond_9_2 = entities.Item([6.25 * SCALE, 12 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_9_1 = entities.Item([12.25 * SCALE, 0 * SCALE], ten_emerald_img, 10)
    ten_emerald_9_2 = entities.Item([7.25 * SCALE, 4 * SCALE], ten_emerald_img, 10)
    ten_emerald_9_3 = entities.Item([7.25 * SCALE, 10 * SCALE], ten_emerald_img, 10)
    ten_emerald_9_4 = entities.Item([9.25 * SCALE, 12 * SCALE], ten_emerald_img, 10)
    '''$5'''
    five_coin_9_1 = entities.Item([4.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_9_2 = entities.Item([3.25 * SCALE, 1 * SCALE], five_coin_img, 5)
    five_coin_9_3 = entities.Item([12.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_9_4 = entities.Item([0.25 * SCALE, 8 * SCALE], five_coin_img, 5)
    five_coin_9_5 = entities.Item([1.25 * SCALE, 8 * SCALE], five_coin_img, 5)
    five_coin_9_6 = entities.Item([0.25 * SCALE, 9 * SCALE], five_coin_img, 5)
    five_coin_9_7 = entities.Item([1.25 * SCALE, 9 * SCALE], five_coin_img, 5)
    five_coin_9_8 = entities.Item([6.25 * SCALE, 10 * SCALE], five_coin_img, 5)
    five_coin_9_9 = entities.Item([10.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_9_1 = entities.Item([6.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_9_2 = entities.Item([6.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_9_3 = entities.Item([0.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_9_4 = entities.Item([1.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_9_5 = entities.Item([6.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_9_6 = entities.Item([3.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_9_7 = entities.Item([4.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_9_8 = entities.Item([3.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_9_9 = entities.Item([4.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_9_10 = entities.Item([13.25 * SCALE, 5 * SCALE], a_coin_img, 1)
    one_coin_9_11 = entities.Item([3.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_9_12 = entities.Item([4.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_9_13 = entities.Item([13.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_9_14 = entities.Item([3.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_9_15 = entities.Item([4.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_9_16 = entities.Item([13.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_9_17 = entities.Item([9.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_9_18 = entities.Item([3.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_9_19 = entities.Item([4.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_9_20 = entities.Item([9.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_9_21 = entities.Item([3.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_9_22 = entities.Item([4.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_9_23 = entities.Item([9.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_9_24 = entities.Item([1.25 * SCALE, 11 * SCALE], a_coin_img, 1)
    one_coin_9_25 = entities.Item([1.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_9_26 = entities.Item([1.25 * SCALE, 13 * SCALE], a_coin_img, 1)

         # FLOOR 8 COINS
    '''$15'''
    fifteen_diamond_8_1 = entities.Item([3.25 * SCALE, 10 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_8_1 = entities.Item([6.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_2 = entities.Item([8.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_3 = entities.Item([8.25 * SCALE, 6.5 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_4 = entities.Item([9.25 * SCALE, 6.5 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_5 = entities.Item([10.25 * SCALE, 6.5 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_6 = entities.Item([9.25 * SCALE, 9 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_7 = entities.Item([4.25 * SCALE, 10 * SCALE], ten_emerald_img, 5)
    ten_emerald_8_8 = entities.Item([0.25 * SCALE, 13 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_8_1 = entities.Item([5.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_8_2 = entities.Item([7.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_8_3 = entities.Item([0.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_8_4 = entities.Item([1.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_8_5 = entities.Item([6.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_8_6 = entities.Item([0.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_8_7 = entities.Item([7.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_8_8 = entities.Item([7.25 * SCALE, 8 * SCALE], five_coin_img, 5)
    five_coin_8_9 = entities.Item([7.25 * SCALE, 9 * SCALE], five_coin_img, 5)
    five_coin_8_10 = entities.Item([12.25 * SCALE, 10 * SCALE], five_coin_img, 5)
    five_coin_8_11 = entities.Item([1.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_8_1 = entities.Item([1.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_8_2 = entities.Item([2.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_8_3 = entities.Item([12.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_8_4 = entities.Item([1.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_8_5 = entities.Item([2.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_8_6 = entities.Item([12.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_8_7 = entities.Item([12.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_8_8 = entities.Item([9.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_8_9 = entities.Item([10.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_8_10 = entities.Item([9.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_8_11 = entities.Item([10.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_8_12 = entities.Item([3.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_8_13 = entities.Item([4.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_8_14 = entities.Item([1.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_8_15 = entities.Item([3.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_8_16 = entities.Item([4.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_8_17 = entities.Item([1.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_8_18 = entities.Item([1.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_8_19 = entities.Item([3.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_8_20 = entities.Item([6.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_8_21 = entities.Item([7.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_8_22 = entities.Item([3.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_8_23 = entities.Item([6.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_8_24 = entities.Item([7.25 * SCALE, 13 * SCALE], a_coin_img, 1)

         # FLOOR 7 COINS
    '''$15'''
    fifteen_diamond_7_1 = entities.Item([4.25 * SCALE, 0 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_7_1 = entities.Item([11.25 * SCALE, 0 * SCALE], ten_emerald_img, 5)
    ten_emerald_7_2 = entities.Item([8.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_7_3 = entities.Item([4.25 * SCALE, 7 * SCALE], ten_emerald_img, 5)
    ten_emerald_7_4 = entities.Item([6.25 * SCALE, 7 * SCALE], ten_emerald_img, 5)
    ten_emerald_7_5 = entities.Item([12.25 * SCALE, 9 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_7_1 = entities.Item([8.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_7_2 = entities.Item([11.25 * SCALE, 1 * SCALE], five_coin_img, 5)
    five_coin_7_3 = entities.Item([13.25 * SCALE, 2 * SCALE], five_coin_img, 5)
    five_coin_7_4 = entities.Item([5.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_7_5 = entities.Item([12.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_7_6 = entities.Item([9.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_7_7 = entities.Item([13.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_7_8 = entities.Item([3.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_7_1 = entities.Item([3.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_7_2 = entities.Item([6.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_7_3 = entities.Item([2.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_7_4 = entities.Item([7.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_7_5 = entities.Item([6.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_7_6 = entities.Item([7.25 * SCALE, 5 * SCALE], a_coin_img, 1)
    one_coin_7_7 = entities.Item([2.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_7_8 = entities.Item([13.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_7_9 = entities.Item([1.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_7_10 = entities.Item([12.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_7_11 = entities.Item([0.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_7_12 = entities.Item([5.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_7_13 = entities.Item([9.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_7_14 = entities.Item([10.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_7_15 = entities.Item([0.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_7_16 = entities.Item([1.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_7_17 = entities.Item([5.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_7_18 = entities.Item([9.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_7_19 = entities.Item([10.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_7_20 = entities.Item([0.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_7_21 = entities.Item([1.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_7_22 = entities.Item([6.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_7_23 = entities.Item([8.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_7_24 = entities.Item([9.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_7_25 = entities.Item([10.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_7_26 = entities.Item([0.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_7_27 = entities.Item([1.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_7_28 = entities.Item([6.25 * SCALE, 13 * SCALE], a_coin_img, 1)

         # FLOOR 6 COINS
    '''$15'''
    fifteen_diamond_6_1 = entities.Item([13.25 * SCALE, 13 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_6_1 = entities.Item([9.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_2 = entities.Item([4.25 * SCALE, 6 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_3 = entities.Item([7.25 * SCALE, 7 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_4 = entities.Item([7.25 * SCALE, 12 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_5 = entities.Item([9.25 * SCALE, 12 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_6 = entities.Item([1.25 * SCALE, 13 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_7 = entities.Item([3.25 * SCALE, 13 * SCALE], ten_emerald_img, 5)
    ten_emerald_6_8 = entities.Item([5.25 * SCALE, 13 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_6_1 = entities.Item([3.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_6_2 = entities.Item([5.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_6_3 = entities.Item([11.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_6_4 = entities.Item([12.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_6_5 = entities.Item([6.25 * SCALE, 9 * SCALE], five_coin_img, 5)
    five_coin_6_6 = entities.Item([7.25 * SCALE, 10 * SCALE], five_coin_img, 5)
    five_coin_6_7 = entities.Item([0.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    five_coin_6_8 = entities.Item([4.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    five_coin_6_9 = entities.Item([10.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_6_1 = entities.Item([2.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_6_2 = entities.Item([5.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_6_3 = entities.Item([6.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_6_4 = entities.Item([7.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_6_5 = entities.Item([12.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_6_6 = entities.Item([13.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_6_7 = entities.Item([0.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_6_8 = entities.Item([0.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_6_9 = entities.Item([6.25 * SCALE, 5 * SCALE], a_coin_img, 1)
    one_coin_6_10 = entities.Item([7.25 * SCALE, 5 * SCALE], a_coin_img, 1)
    one_coin_6_11 = entities.Item([1.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_6_12 = entities.Item([1.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_6_13 = entities.Item([13.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_6_14 = entities.Item([0.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_6_15 = entities.Item([9.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_6_16 = entities.Item([12.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_6_17 = entities.Item([0.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_6_18 = entities.Item([3.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_6_19 = entities.Item([9.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_6_20 = entities.Item([11.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    
         # FLOOR 5 COINS
    '''$15'''
    fifteen_diamond_5_1 = entities.Item([3.25 * SCALE, 3 * SCALE], fifteen_diamond_img, 15)
    fifteen_diamond_5_2 = entities.Item([4.25 * SCALE, 3 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_5_1 = entities.Item([7.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_5_2 = entities.Item([1.25 * SCALE, 5 * SCALE], ten_emerald_img, 5)
    ten_emerald_5_3 = entities.Item([3.25 * SCALE, 6 * SCALE], ten_emerald_img, 5)
    ten_emerald_5_4 = entities.Item([0.25 * SCALE, 8 * SCALE], ten_emerald_img, 5)
    ten_emerald_5_5 = entities.Item([1.25 * SCALE, 8 * SCALE], ten_emerald_img, 5)
    ten_emerald_5_6 = entities.Item([3.25 * SCALE, 12 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_5_1 = entities.Item([3.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_5_2 = entities.Item([4.25 * SCALE, 1 * SCALE], five_coin_img, 5)
    five_coin_5_3 = entities.Item([6.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_5_4 = entities.Item([7.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_5_5 = entities.Item([0.25 * SCALE, 5 * SCALE], five_coin_img, 5)
    five_coin_5_6 = entities.Item([12.25 * SCALE, 5 * SCALE], five_coin_img, 5)
    five_coin_5_7 = entities.Item([6.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_5_8 = entities.Item([7.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_5_9 = entities.Item([12.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_5_10 = entities.Item([9.25 * SCALE, 8 * SCALE], five_coin_img, 5)
    five_coin_5_11 = entities.Item([10.25 * SCALE, 8 * SCALE], five_coin_img, 5)
    five_coin_5_12 = entities.Item([6.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_5_1 = entities.Item([12.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_5_2 = entities.Item([12.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_5_3 = entities.Item([10.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_5_4 = entities.Item([9.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_5_5 = entities.Item([12.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_5_6 = entities.Item([4.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_5_7 = entities.Item([4.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_5_8 = entities.Item([12.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_5_9 = entities.Item([4.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_5_10 = entities.Item([13.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_5_11 = entities.Item([0.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_5_12 = entities.Item([1.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_5_13 = entities.Item([9.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_5_14 = entities.Item([0.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_5_15 = entities.Item([1.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_5_16 = entities.Item([9.25 * SCALE, 13 * SCALE], a_coin_img, 1)

         # FLOOR 4 COINS
    '''$15'''
    fifteen_diamond_4_1 = entities.Item([6.25 * SCALE, 9 * SCALE], fifteen_diamond_img, 15)
    fifteen_diamond_4_2 = entities.Item([12.25 * SCALE, 12 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_4_1 = entities.Item([6.25 * SCALE, 3 * SCALE], ten_emerald_img, 5)
    ten_emerald_4_2 = entities.Item([13.25 * SCALE, 3 * SCALE], ten_emerald_img, 5)
    ten_emerald_4_3 = entities.Item([7.25 * SCALE, 5 * SCALE], ten_emerald_img, 5)
    ten_emerald_4_4 = entities.Item([6.25 * SCALE, 6 * SCALE], ten_emerald_img, 5)
    ten_emerald_4_5 = entities.Item([13.25 * SCALE, 10 * SCALE], ten_emerald_img, 5)
    ten_emerald_4_6 = entities.Item([9.25 * SCALE, 12 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_4_1 = entities.Item([3.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_4_2 = entities.Item([8.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_4_3 = entities.Item([8.25 * SCALE, 1 * SCALE], five_coin_img, 5)
    five_coin_4_4 = entities.Item([9.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_4_5 = entities.Item([10.25 * SCALE, 5 * SCALE], five_coin_img, 5)
    five_coin_4_6 = entities.Item([3.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_4_7 = entities.Item([9.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_4_8 = entities.Item([12.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_4_9 = entities.Item([12.25 * SCALE, 10 * SCALE], five_coin_img, 5)
    five_coin_4_10 = entities.Item([5.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    five_coin_4_11 = entities.Item([7.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_4_1 = entities.Item([11.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_4_2 = entities.Item([12.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_4_3 = entities.Item([13.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_4_4 = entities.Item([0.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_4_5 = entities.Item([0.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_4_6 = entities.Item([0.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_4_7 = entities.Item([3.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_4_8 = entities.Item([4.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_4_9 = entities.Item([10.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_4_10 = entities.Item([1.25 * SCALE, 5 * SCALE], a_coin_img, 1)
    one_coin_4_11 = entities.Item([9.25 * SCALE, 5 * SCALE], a_coin_img, 1)
    one_coin_4_12 = entities.Item([1.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_4_13 = entities.Item([10.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_4_14 = entities.Item([1.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_4_15 = entities.Item([0.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_4_16 = entities.Item([0.25 * SCALE, 11 * SCALE], a_coin_img, 1)
    one_coin_4_17 = entities.Item([0.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_4_18 = entities.Item([2.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_4_19 = entities.Item([2.25 * SCALE, 13 * SCALE], a_coin_img, 1)

     # FLOOR 3 COINS
    '''$15'''
    fifteen_diamond_3_1 = entities.Item([12.25 * SCALE, 3 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_3_1 = entities.Item([12.25 * SCALE, 0 * SCALE], ten_emerald_img, 5)
    ten_emerald_3_2 = entities.Item([12.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_3_3 = entities.Item([0.25 * SCALE, 3 * SCALE], ten_emerald_img, 5)
    ten_emerald_3_4 = entities.Item([6.25 * SCALE, 9 * SCALE], ten_emerald_img, 5)
    ten_emerald_3_5 = entities.Item([5.25 * SCALE, 13 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_3_1 = entities.Item([3.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_3_2 = entities.Item([8.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_3_3 = entities.Item([0.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_3_4 = entities.Item([1.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_3_5 = entities.Item([8.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_3_6 = entities.Item([0.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    five_coin_3_7 = entities.Item([5.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_3_1 = entities.Item([2.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_3_2 = entities.Item([3.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_3_3 = entities.Item([6.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_3_4 = entities.Item([4.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_3_5 = entities.Item([6.25 * SCALE, 2 * SCALE], a_coin_img, 1)
    one_coin_3_6 = entities.Item([6.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_3_7 = entities.Item([12.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_3_8 = entities.Item([13.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_3_9 = entities.Item([2.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_3_10 = entities.Item([3.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_3_11 = entities.Item([10.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_3_12 = entities.Item([11.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_3_13 = entities.Item([2.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_3_14 = entities.Item([4.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_3_15 = entities.Item([10.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_3_16 = entities.Item([11.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    
     # FLOOR 2 COINS
    '''$15'''
    fifteen_diamond_2_1 = entities.Item([0.25 * SCALE, 12 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_2_1 = entities.Item([6.25 * SCALE, 0 * SCALE], ten_emerald_img, 5)
    ten_emerald_2_2 = entities.Item([4.25 * SCALE, 6 * SCALE], ten_emerald_img, 5)
    ten_emerald_2_3 = entities.Item([10.25 * SCALE, 6 * SCALE], ten_emerald_img, 5)
    ten_emerald_2_4 = entities.Item([1.25 * SCALE, 9 * SCALE], ten_emerald_img, 5)
    ten_emerald_2_5 = entities.Item([6.25 * SCALE, 9 * SCALE], ten_emerald_img, 5)
    ten_emerald_2_6 = entities.Item([1.25 * SCALE, 10 * SCALE], ten_emerald_img, 5)
    ten_emerald_2_7 = entities.Item([0.25 * SCALE, 13 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_2_1 = entities.Item([7.25 * SCALE, 0 * SCALE], five_coin_img, 5)
    five_coin_2_2 = entities.Item([6.25 * SCALE, 1 * SCALE], five_coin_img, 5)
    five_coin_2_3 = entities.Item([1.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_2_4 = entities.Item([3.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_2_5 = entities.Item([7.25 * SCALE, 3 * SCALE], five_coin_img, 5)
    five_coin_2_6 = entities.Item([0.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_2_7 = entities.Item([6.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_2_8 = entities.Item([12.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_2_9 = entities.Item([12.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_2_10 = entities.Item([13.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_2_11 = entities.Item([12.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    five_coin_2_12 = entities.Item([13.25 * SCALE, 13 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_2_1 = entities.Item([3.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_2_2 = entities.Item([4.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_2_3 = entities.Item([11.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_2_4 = entities.Item([12.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_2_5 = entities.Item([3.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_2_6 = entities.Item([4.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_2_7 = entities.Item([11.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_2_8 = entities.Item([12.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_2_9 = entities.Item([6.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_2_10 = entities.Item([7.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_2_11 = entities.Item([8.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_2_12 = entities.Item([6.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_2_13 = entities.Item([7.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_2_14 = entities.Item([8.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_2_15 = entities.Item([3.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_2_16 = entities.Item([9.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_2_17 = entities.Item([10.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_2_18 = entities.Item([11.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_2_19 = entities.Item([4.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_2_20 = entities.Item([10.25 * SCALE, 11 * SCALE], a_coin_img, 1)
    one_coin_2_21 = entities.Item([3.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_2_22 = entities.Item([4.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_2_23 = entities.Item([9.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_2_24 = entities.Item([3.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_2_25 = entities.Item([4.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_2_26 = entities.Item([8.25 * SCALE, 13 * SCALE], a_coin_img, 1)



         # FLOOR 1 COINS
    '''$15'''
    fifteen_diamond_1_1 = entities.Item([6.25 * SCALE, 9 * SCALE], fifteen_diamond_img, 15)
    '''$10'''
    ten_emerald_1_1 = entities.Item([3.25 * SCALE, 0 * SCALE], ten_emerald_img, 5)
    ten_emerald_1_2 = entities.Item([3.25 * SCALE, 1 * SCALE], ten_emerald_img, 5)
    ten_emerald_1_3 = entities.Item([9.25 * SCALE, 5 * SCALE], ten_emerald_img, 5)
    ten_emerald_1_4 = entities.Item([6.25 * SCALE, 10 * SCALE], ten_emerald_img, 5)
    '''$5'''
    five_coin_1_1 = entities.Item([6.25 * SCALE, 1 * SCALE], five_coin_img, 5)
    five_coin_1_2 = entities.Item([0.25 * SCALE, 4 * SCALE], five_coin_img, 5)
    five_coin_1_3 = entities.Item([3.25 * SCALE, 6 * SCALE], five_coin_img, 5)
    five_coin_1_4 = entities.Item([4.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_1_5 = entities.Item([12.25 * SCALE, 7 * SCALE], five_coin_img, 5)
    five_coin_1_6 = entities.Item([12.25 * SCALE, 12 * SCALE], five_coin_img, 5)
    '''$1'''
    one_coin_1_1 = entities.Item([1.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_1_2 = entities.Item([9.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_1_3 = entities.Item([10.25 * SCALE, 0 * SCALE], a_coin_img, 1)
    one_coin_1_4 = entities.Item([0.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_1_5 = entities.Item([9.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_1_6 = entities.Item([10.25 * SCALE, 1 * SCALE], a_coin_img, 1)
    one_coin_1_7 = entities.Item([3.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_1_8 = entities.Item([6.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_1_9 = entities.Item([7.25 * SCALE, 3 * SCALE], a_coin_img, 1)
    one_coin_1_10 = entities.Item([6.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_1_11 = entities.Item([7.25 * SCALE, 4 * SCALE], a_coin_img, 1)
    one_coin_1_12 = entities.Item([6.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_1_13 = entities.Item([7.25 * SCALE, 6 * SCALE], a_coin_img, 1)
    one_coin_1_14 = entities.Item([6.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_1_15 = entities.Item([7.25 * SCALE, 7 * SCALE], a_coin_img, 1)
    one_coin_1_16 = entities.Item([9.25 * SCALE, 8 * SCALE], a_coin_img, 1)
    one_coin_1_17 = entities.Item([10.25 * SCALE, 9 * SCALE], a_coin_img, 1)
    one_coin_1_18 = entities.Item([0.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_1_19 = entities.Item([1.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_1_20 = entities.Item([11.25 * SCALE, 10 * SCALE], a_coin_img, 1)
    one_coin_1_21 = entities.Item([0.25 * SCALE, 11 * SCALE], a_coin_img, 1)
    one_coin_1_22 = entities.Item([1.25 * SCALE, 11 * SCALE], a_coin_img, 1)
    one_coin_1_23 = entities.Item([3.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_1_24 = entities.Item([4.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_1_25 = entities.Item([8.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_1_26 = entities.Item([9.25 * SCALE, 12 * SCALE], a_coin_img, 1)
    one_coin_1_27 = entities.Item([3.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_1_28 = entities.Item([4.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_1_29 = entities.Item([8.25 * SCALE, 13 * SCALE], a_coin_img, 1)
    one_coin_1_30 = entities.Item([9.25 * SCALE, 13 * SCALE], a_coin_img, 1)


    items = pygame.sprite.Group()

        # Goals
    g10 = entities.Goal([6.25 * SCALE, 9.25 * SCALE], goal_img)
    g9 = entities.Goal([9.25 * SCALE, 0.25 * SCALE], goal_img)
    g8 = entities.Goal([12.25 * SCALE, 6.25 * SCALE], goal_img)
    g7 = entities.Goal([9.25 * SCALE, 3.25 * SCALE], goal_img)
    g6 = entities.Goal([9.25 * SCALE, 6.25 * SCALE], goal_img)
    g5 = entities.Goal([0.25 * SCALE, 9.25 * SCALE], goal_img)
    g4 = entities.Goal([3.25 * SCALE, 9.25 * SCALE], goal_img)
    g3 = entities.Goal([9.25 * SCALE, 3.25 * SCALE], goal_img)
    g2 = entities.Goal([0.25 * SCALE, 6.25 * SCALE], goal_img)
    g1 = entities.Goal([6.25 * SCALE, 12.75 * SCALE], floor_1_goal_img)
    goals = pygame.sprite.Group()
    

        # Full Levels
    if floor == 10:
        walls.add(w0_1, w0_2, w0_3)
        goals.add(g10)

    elif floor == 9:
        walls.add(w1_1, w1_2, w1_3, w1_4, w1_5, w1_6, w1_7, w1_8, w1_9, w1_10)
        
        items.add(fifteen_diamond_9_1, fifteen_diamond_9_2, 

                  ten_emerald_9_1, ten_emerald_9_2, ten_emerald_9_3, ten_emerald_9_4, 

                  five_coin_9_1, five_coin_9_2, five_coin_9_3, five_coin_9_4, five_coin_9_5, 
                  five_coin_9_6, five_coin_9_7, five_coin_9_8, five_coin_9_9, 

                  one_coin_9_1, one_coin_9_2, one_coin_9_3, one_coin_9_4, one_coin_9_5, 
                  one_coin_9_6, one_coin_9_7, one_coin_9_8, one_coin_9_9, one_coin_9_10, 
                  one_coin_9_11, one_coin_9_12, one_coin_9_13, one_coin_9_14, one_coin_9_15,
                  one_coin_9_16, one_coin_9_17, one_coin_9_18, one_coin_9_19, one_coin_9_20, 
                  one_coin_9_21, one_coin_9_22, one_coin_9_23, one_coin_9_24, one_coin_9_25, 
                  one_coin_9_26)
        
        goals.add(g9)
        
    elif floor == 8:
        walls.add(w2_1, w2_2, w2_3, w2_4, w2_5, w2_6, w2_7, w2_8)

        items.add(fifteen_diamond_8_1, 

                  ten_emerald_8_1, ten_emerald_8_2, ten_emerald_8_3, ten_emerald_8_4, ten_emerald_8_5, 
                  ten_emerald_8_6, ten_emerald_8_7, ten_emerald_8_8, 

                  five_coin_8_1, five_coin_8_2, five_coin_8_3, five_coin_8_4, five_coin_8_5, 
                  five_coin_8_6, five_coin_8_7, five_coin_8_8, five_coin_8_9, five_coin_8_10, 
                  five_coin_8_11, 

                  one_coin_8_1, one_coin_8_2, one_coin_8_3, one_coin_8_4, one_coin_8_5, 
                  one_coin_8_6, one_coin_8_7, one_coin_8_8, one_coin_8_9, one_coin_8_10, 
                  one_coin_8_11, one_coin_8_12, one_coin_8_13, one_coin_8_14, one_coin_8_15, 
                  one_coin_8_16, one_coin_8_17, one_coin_8_18, one_coin_8_19, one_coin_8_20, 
                  one_coin_8_21, one_coin_8_22, one_coin_8_23, one_coin_8_24)
        
        goals.add(g8)
        
    elif floor == 7:
        walls.add(w3_1, w3_2, w3_3, w3_4, w3_5, w3_6, w3_7, w3_8, w3_9, w3_10, w3_11)

        items.add(fifteen_diamond_7_1, 

                  ten_emerald_7_1, ten_emerald_7_2, ten_emerald_7_3, ten_emerald_7_4, ten_emerald_7_5,  

                  five_coin_7_1, five_coin_7_2, five_coin_7_3, five_coin_7_4, five_coin_7_5, 
                  five_coin_7_6, five_coin_7_7, five_coin_7_8, 

                  one_coin_7_1, one_coin_7_2, one_coin_7_3, one_coin_7_4, one_coin_7_5, 
                  one_coin_7_6, one_coin_7_7, one_coin_7_8, one_coin_7_9, one_coin_7_10, 
                  one_coin_7_11, one_coin_7_12, one_coin_7_13, one_coin_7_14, one_coin_7_15, 
                  one_coin_7_16, one_coin_7_17, one_coin_7_18, one_coin_7_19, one_coin_7_20, 
                  one_coin_7_21, one_coin_7_22, one_coin_7_23, one_coin_7_24, one_coin_7_25, 
                  one_coin_7_26, one_coin_7_27, one_coin_7_28)

        goals.add(g7)
        
    elif floor == 6:
        walls.add(w4_1, w4_2, w4_3, w4_4, w4_5, w4_6, w4_7, w4_8)
        
        items.add(fifteen_diamond_6_1, 

                  ten_emerald_6_1, ten_emerald_6_2, ten_emerald_6_3, ten_emerald_6_4, ten_emerald_6_5, 
                  ten_emerald_6_6, ten_emerald_6_7, ten_emerald_6_8, 

                  five_coin_6_1, five_coin_6_2, five_coin_6_3, five_coin_6_4, five_coin_6_5, 
                  five_coin_6_6, five_coin_6_7, five_coin_6_8, five_coin_6_9,  

                  one_coin_6_1, one_coin_6_2, one_coin_6_3, one_coin_6_4, one_coin_6_5, 
                  one_coin_6_6, one_coin_6_7, one_coin_6_8, one_coin_6_9, one_coin_6_10, 
                  one_coin_6_11, one_coin_6_12, one_coin_6_13, one_coin_6_14, one_coin_6_15, 
                  one_coin_6_16, one_coin_6_17, one_coin_6_18, one_coin_6_19, one_coin_6_20)

        goals.add(g6)
        
    elif floor == 5:
        walls.add(w5_1, w5_2, w5_3, w5_4, w5_5, w5_6, w5_7, w5_8, w5_9)
        
        items.add(fifteen_diamond_5_1, fifteen_diamond_5_2, 

                  ten_emerald_5_1, ten_emerald_5_2, ten_emerald_5_3, ten_emerald_5_4, ten_emerald_5_5, 
                  ten_emerald_5_6, 

                  five_coin_5_1, five_coin_5_2, five_coin_5_3, five_coin_5_4, five_coin_5_5, 
                  five_coin_5_6, five_coin_5_7, five_coin_5_8, five_coin_5_9, five_coin_5_10,
                  five_coin_5_11, five_coin_5_12, 

                  one_coin_5_1, one_coin_5_2, one_coin_5_3, one_coin_5_4, one_coin_5_5, 
                  one_coin_5_6, one_coin_5_7, one_coin_5_8, one_coin_5_9, one_coin_5_10, 
                  one_coin_5_11, one_coin_5_12, one_coin_5_13, one_coin_5_14, one_coin_5_15, 
                  one_coin_5_16)

        goals.add(g5)
        
    elif floor == 4:
        walls.add(w6_1, w6_2, w6_3, w6_4, w6_5, w6_6, w6_7, w6_8, w6_9)
        
        items.add(fifteen_diamond_4_1, fifteen_diamond_4_2, 

                  ten_emerald_4_1, ten_emerald_4_2, ten_emerald_4_3, ten_emerald_4_4, ten_emerald_4_5, 
                  ten_emerald_4_6, 

                  five_coin_4_1, five_coin_4_2, five_coin_4_3, five_coin_4_4, five_coin_4_5, 
                  five_coin_4_6, five_coin_4_7, five_coin_4_8, five_coin_4_9, five_coin_4_10,
                  five_coin_4_11, 

                  one_coin_4_1, one_coin_4_2, one_coin_4_3, one_coin_4_4, one_coin_4_5, 
                  one_coin_4_6, one_coin_4_7, one_coin_4_8, one_coin_4_9, one_coin_4_10, 
                  one_coin_4_11, one_coin_4_12, one_coin_4_13, one_coin_4_14, one_coin_4_15, 
                  one_coin_4_16, one_coin_4_17, one_coin_4_18, one_coin_4_19)

        goals.add(g4)
        
    elif floor == 3:
        walls.add(w7_1, w7_2, w7_3, w7_4, w7_5, w7_6, w7_7, w7_8, w7_9, w7_10)
        
        items.add(fifteen_diamond_3_1, 

                  ten_emerald_3_1, ten_emerald_3_2, ten_emerald_3_3, ten_emerald_3_4, ten_emerald_3_5,  

                  five_coin_3_1, five_coin_3_2, five_coin_3_3, five_coin_3_4, five_coin_3_5, 
                  five_coin_3_6, five_coin_3_7, 

                  one_coin_3_1, one_coin_3_2, one_coin_3_3, one_coin_3_4, one_coin_3_5, 
                  one_coin_3_6, one_coin_3_7, one_coin_3_8, one_coin_3_9, one_coin_3_10, 
                  one_coin_3_11, one_coin_3_12, one_coin_3_13, one_coin_3_14, one_coin_3_15, 
                  one_coin_3_16)

        goals.add(g3)
        
    elif floor == 2:
        walls.add(w8_1, w8_2, w8_3, w8_4, w8_5, w8_6, w8_7, w8_8, w8_9, w8_10)
        
        items.add(fifteen_diamond_2_1, 

                  ten_emerald_2_1, ten_emerald_2_2, ten_emerald_2_3, ten_emerald_2_4, ten_emerald_2_5, 
                  ten_emerald_2_6, ten_emerald_2_7, 

                  five_coin_2_1, five_coin_2_2, five_coin_2_3, five_coin_2_4, five_coin_2_5, 
                  five_coin_2_6, five_coin_2_7, five_coin_2_8, five_coin_2_9, five_coin_2_10,
                  five_coin_2_11, five_coin_2_12, 

                  one_coin_2_1, one_coin_2_2, one_coin_2_3, one_coin_2_4, one_coin_2_5, 
                  one_coin_2_6, one_coin_2_7, one_coin_2_8, one_coin_2_9, one_coin_2_10, 
                  one_coin_2_11, one_coin_2_12, one_coin_2_13, one_coin_2_14, one_coin_2_15, 
                  one_coin_2_16, one_coin_2_17, one_coin_2_18, one_coin_2_19, one_coin_2_20, 
                  one_coin_2_21, one_coin_2_22, one_coin_2_23, one_coin_2_24, one_coin_2_25,
                  one_coin_2_26)

        goals.add(g2)
        
    elif floor == 1:
        walls.add(w9_1, w9_2, w9_3, w9_4, w9_5, w9_6, w9_7, w9_8, w9_9, w9_10)
        
        items.add(fifteen_diamond_1_1, 

                  ten_emerald_1_1, ten_emerald_1_2, ten_emerald_1_3, ten_emerald_1_4, 

                  five_coin_1_1, five_coin_1_2, five_coin_1_3, five_coin_1_4, five_coin_1_5, 
                  five_coin_1_6, 

                  one_coin_1_1, one_coin_1_2, one_coin_1_3, one_coin_1_4, one_coin_1_5, 
                  one_coin_1_6, one_coin_1_7, one_coin_1_8, one_coin_1_9, one_coin_1_10, 
                  one_coin_1_11, one_coin_1_12, one_coin_1_13, one_coin_1_14, one_coin_1_15, 
                  one_coin_1_16, one_coin_1_17, one_coin_1_18, one_coin_1_19, one_coin_1_20, 
                  one_coin_1_21, one_coin_1_22, one_coin_1_23, one_coin_1_24, one_coin_1_25, 
                  one_coin_1_26, one_coin_1_27, one_coin_1_28, one_coin_1_29, one_coin_1_30)

        goals.add(g1)
    
    

    if show_start_screen_again == False:
        current_scene = PLAYING
    else:
        current_scene = START


    # Text Functions
def write_sm(text, color, x, y):
    text1 = FONT_SM.render(text, True, color)
    screen.blit(text1, [x, y])
    
def write_md(text, color, x, y):
    text1 = FONT_MD.render(text, True, color)
    screen.blit(text1, [x, y])
    
def write_lg(text, color, x, y):
    text1 = FONT_LG.render(text, True, color)
    screen.blit(text1, [x, y])

    # Start and Level Transition Screens
def play_cutscene():
    global current_scene, cutscene_img
    current_scene = CUTSCENE
    cutscene_img = 1

def play_game():
    global current_scene
    current_scene = PLAYING
    if floor > 0:
        play_fuzzy_time_mine()

def next_level():
    global current_scene, floor
    floor -= 1
    current_scene = LEVEL_TRANSITION
    p1.reached_goal = False

def show_start_screen():
    upload_start_screen()

def show_hud(color, rect_color):
    # Coin Count
    subtext = FONT_MD.render(f"$ {p1.score * 100}", True, color)
    rect = subtext.get_rect()
    rect.topleft = SCALE // 10, SCALE // 5
    screen.blit(subtext, rect)
    # Timer
    subtext = FONT_MD.render(f"TIME: {p1.timer // FPS}", True, color)
    rect = subtext.get_rect()
    rect.midtop = WIDTH // 2, SCALE // 5
    screen.blit(subtext, rect)
    # Floor
    subtext = FONT_MD.render(f"Floor = {floor}", True, color)
    rect = subtext.get_rect()
    rect.topright = WIDTH - SCALE // 10, SCALE // 5
    screen.blit(subtext, rect)

def show_next_level_screen(color):
    if floor == 0:
        title_text = FONT_EXIT_TOWER.render("CONGRATS! You've escaped the tower!", True, color)
    else:
        title_text = FONT_MD.render("Ready for the next floor?", True, color)
    rect = title_text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT //2 - 100
    screen.blit(title_text, rect)

    subtext = FONT_FINAL_SCORE.render("Press SPACE", True, color)
    rect = subtext.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT //2 - 90
    screen.blit(subtext, rect)

def show_lose_screen(color):
    upload_lose_screen()

    subtext = FONT_FINAL_SCORE.render(f" SCORE: ${p1.score * 100}", True, color)
    rect = subtext.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 3
    screen.blit(subtext, rect)

def show_win_game_screen(color):
    if p1.score > 700:
        upload_winner_screen()
    elif p1.score > 300:
        upload_nice_work_screen()
    else:
        upload_try_again_screen()
        

    subtext = FONT_FINAL_SCORE.render(f" SCORE: ${p1.score * 100}", True, color)
    rect = subtext.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 3
    screen.blit(subtext, rect)

def show_cutscenes():
    global current_scene, cutscene_img
    
    if current_scene == CUTSCENE:
        if cutscene_img == 1:
            upload_cutscene_1()
        elif cutscene_img == 2:
            upload_cutscene_2()
        elif cutscene_img == 3:
            upload_cutscene_3()
        elif cutscene_img == 4:
            upload_cutscene_4()
        elif cutscene_img == 5:
            upload_cutscene_5()
        elif cutscene_img == 6:
            upload_cutscene_6()
        elif cutscene_img == 7:
            upload_cutscene_7()
        elif cutscene_img == 8:
            upload_cutscene_8()
        elif cutscene_img == 9:
            upload_cutscene_9()
        elif cutscene_img == 10:
            upload_cutscene_10()
        elif cutscene_img == 11:
            upload_cutscene_instruct()


# Game loop
new_game()
running = True

while running:
    '''Input handling'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            
            #Start Screen
            if event.type == pygame.KEYDOWN:
                if current_scene == START:
                    if event.key == pygame.K_SPACE:
                        play_cutscene()
                elif current_scene == CUTSCENE:
                    if event.key == pygame.K_SPACE:
                        if cutscene_img < 11:
                            cutscene_img += 1
                        else:
                            play_game()

                # Next Level Screen
                elif current_scene == LEVEL_TRANSITION:
                    if event.key == pygame.K_SPACE:
                        start_a_level()
                
                # Lose Screen
                elif current_scene == LOSE:
                    if event.key == pygame.K_SPACE:
                        new_game()
                
                # Win Game Screen
                elif current_scene == WIN_GAME:
                    if event.key == pygame.K_SPACE:
                        new_game()
            
    pressed = pygame.key.get_pressed()

    '''Movement P1'''
    p1.dash_stop()

    if pressed[pygame.K_UP] and pressed[pygame.K_DOWN]:
        p1.stop_y()
    elif pressed[pygame.K_UP]:
        p1.move_up()
    elif pressed[pygame.K_DOWN]:
        p1.move_down()
    else:
        p1.stop_y()

    if pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]:
        p1.stop_x()
    elif pressed[pygame.K_RIGHT]:
        p1.move_right()
    elif pressed[pygame.K_LEFT]:
        p1.move_left()
    else:
        p1.stop_x()

    # Game logic
    if current_scene == PLAYING:
        p1.update(WIDTH, HEIGHT, walls, items, goals)

        #Next Level
        if p1.reached_goal == True:
            next_level()
            show_start_screen_again = False
        #Lose
        elif p1.timer == 0:
            current_scene = LOSE
            play_lose()
            show_start_screen_again = False
        #Win Game
        elif floor == 0:
            current_scene = WIN_GAME
            pygame.mixer.music.stop()
            show_start_screen_again = True
            if p1.score > 40:
                play_winner()
            elif p1.score > 20:
                play_nice_work()
            else:
                play_try_again()

    # Drawing code
    screen.fill(COLOR_BG)
    
    '''Objects'''
    walls.draw(screen)
    items.draw(screen)
    goals.draw(screen)
    players.draw(screen)

    '''HUD'''
    show_hud(BLACK, COLOR_BG)

    '''Screens'''
            #Start
    if current_scene == START:
        show_start_screen()
        pygame.mixer.stop()
            #Cutscene
    if current_scene == CUTSCENE:
        show_cutscenes()
            #Next Level
    if current_scene == LEVEL_TRANSITION:
        show_next_level_screen(GREEN)
            #Lose
    if current_scene == LOSE:
        show_lose_screen(YELLOW)
            #Win Game
    if current_scene == WIN_GAME:
        show_win_game_screen(YELLOW)


    # Update screen
    
    pygame.display.update()
    clock.tick(FPS)


# Close window and quit
pygame.quit()
