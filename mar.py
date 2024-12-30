


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
