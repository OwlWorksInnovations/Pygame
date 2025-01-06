import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_speed = 1000

left_paddle = pygame.Rect(80, 100, 50, 150)
right_paddle = pygame.Rect(1180, 100, 50, 150)

while running:
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Render game here
    fps = clock.get_fps()
    fps_text = f"FPS: {int(fps)}"
    fps_text_surface = pygame.font.Font(None, 36).render(fps_text, True, "white")
    screen.blit(fps_text_surface, (10, 10))

    # Paddles
    pygame.draw.rect(screen, "white", left_paddle)
    pygame.draw.rect(screen, "white", right_paddle)

    keys = pygame.key.get_pressed()
    left_move_direction = pygame.Vector2(0, 0)
    right_move_direction = pygame.Vector2(0, 0)
    
    if keys[pygame.K_w]:
        left_move_direction.y = -1
    if keys[pygame.K_s]:
        left_move_direction.y = 1
    if keys[pygame.K_UP]:
        right_move_direction.y = -1
    if keys[pygame.K_DOWN]:
        right_move_direction.y = 1

    left_paddle.move_ip(0, left_move_direction.y * player_speed * dt)
    right_paddle.move_ip(0, right_move_direction.y * player_speed * dt)

    # Prevent paddles from moving out of the screen
    left_paddle.y = max(0, min(left_paddle.y, screen.get_height() - left_paddle.height))
    right_paddle.y = max(0, min(right_paddle.y, screen.get_height() - right_paddle.height))
    
    pygame.display.flip()

pygame.quit()

