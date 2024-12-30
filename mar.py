

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
