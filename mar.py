player, platforms, False):
        player.vel_y = 0

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Refresh screen
    pygame.display.flip()

pygame.quit()
sys.exit()
