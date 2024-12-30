
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario Lookalike")
clock = pygame.time.Clock()

# Load assets
player_img = pygame.Surface((40, 60))
player_img.fill(BLUE)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - 100
        self.vel_y = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Apply gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Check ground collision
        if self.rect.bottom >= HEIGHT - 40:  # Ground level
            self.rect.bottom = HEIGHT - 40
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_SPEED

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms
ground = Platform(0, HEIGHT - 40, WIDTH, 40)
platforms.add(ground)
all_sprites.add(ground)

floating_platform = Platform(300, HEIGHT - 150, 200, 20)
platforms.add(floating_platform)
all_sprites.add(floating_platform)

# Main game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update
    all_sprites.update()

    # Check collisions
    if pygame.sprite.spritecollide(player, platforms, False):
        player.vel_y = 0

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Refresh screen
    pygame.display.flip()

pygame.quit()
sys.exit()
