import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 350  # pixels per second

while running:
    dt = clock.tick(60) / 1000  # delta time in seconds

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # FPS
    fps = clock.get_fps()
    fps_text = f"FPS: {int(fps)}"
    fps_text_surface = pygame.font.Font(None, 36).render(fps_text, True, "white")
    screen.blit(fps_text_surface, (10, 10))

    # Player
    pygame.draw.circle(screen, "white", player_pos, 40)

    keys = pygame.key.get_pressed()
    move_direction = pygame.Vector2(0, 0)
    if keys[pygame.K_LEFT]:
        move_direction.x = -1
    if keys[pygame.K_RIGHT]:
        move_direction.x = 1
    if keys[pygame.K_UP]:
        move_direction.y = -1
    if keys[pygame.K_DOWN]:
        move_direction.y = 1

    if move_direction.length_squared() > 0:
        move_direction = move_direction.normalize()

    player_pos += move_direction * player_speed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
