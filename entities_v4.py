import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, loc, image):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = loc

        self.vx = 0
        self.vy = 0
        self.base_speed = 6
        self.speed = 6
        self.timer = 100 * 60

        self.score = 0
        self.reached_goal = False
        
    # Movements
    def move_right(self):
        self.vx = self.speed
  
    def move_left(self):
        self.vx = -1 * self.speed

    def stop_x(self):
        self.vx = 0
    
    def move_up(self):
        self.vy = -1 * self.speed

    def move_down(self):
        self.vy = self.speed

    def stop_y(self):
        self.vy = 0

    def dash_stop(self):
        self.speed = self.base_speed

    # Update Functions
    def move_x(self):
        self.rect.x += self.vx

    def move_y(self):
        self.rect.y += self.vy

        # Wall and Screen Collisions
    def check_walls_x(self, walls):
        hit_walls = pygame.sprite.spritecollide(self, walls, False)

        for walls in hit_walls:
            if self.vx > 0:
                self.rect.right = walls.rect.left
            elif self.vx < 0:
                self.rect.left = walls.rect.right

    def check_walls_y(self, walls):
        hit_walls = pygame.sprite.spritecollide(self, walls, False)

        for walls in hit_walls:
            if self.vy < 0:
                self.rect.top = walls.rect.bottom
            elif self.vy > 0:
                self.rect.bottom = walls.rect.top

    def check_screen_edge(self, WIDTH, HEIGHT):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Items
    def check_items(self, items):
        hit_items = pygame.sprite.spritecollide(self, items, False)

        for item in hit_items:
            item.apply(self)

        # Timer
    def ticking_timer(self):
        if self.timer > 0:
            self.timer -= 1

        # Goals
    def check_goals(self, goals):
        hit_goals = pygame.sprite.spritecollide(self, goals, False)

        for goals in hit_goals:
            self.reached_goal = True

        # Update Function
    def update(self, WIDTH, HEIGHT, walls, items, goals):
        self.move_x()
        self.check_walls_x(walls)
        self.move_y()
        self.check_walls_y(walls)
        self.check_items(items)
        self.ticking_timer()
        self.check_goals(goals)
        self.check_screen_edge(WIDTH, HEIGHT)


class Wall(pygame.sprite.Sprite):

    def __init__(self, loc, size, color):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = loc


class Item(pygame.sprite.Sprite):

    def __init__(self, loc, image, value):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = loc
        self.coin_snd = pygame.mixer.Sound('SFX/coin.mp3')
        self.value = value
        
    # Sound Effects (SFX)
    def play_coin(self):
        self.coin_snd.play()

    def apply(self, player):
        player.score += self.value
        self.play_coin()
        self.kill()


class Goal(pygame.sprite.Sprite):

    def __init__(self, loc, image):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = loc
