import pygame
import random
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 350  # pixels per second

screen_height = screen.get_height()
screen_width = screen.get_width()

bullets = []
enemies = []

current_frame = 0
target_frame = 20
counter = 0
fire_rate = 0.2
can_fire = time.time()

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

    bullet_speed = 1000

    # Spawn bullet
    if keys[pygame.K_SPACE] and time.time() > can_fire:
        can_fire = time.time() + fire_rate
        bullet_pos = pygame.Vector2(player_pos.x, player_pos.y - 30)
        bullets.append(bullet_pos)
    
    bullets = [bullet for bullet in bullets if bullet.y > 0]  # Filter bullets
    for bullet_pos in bullets:
        bullet_pos.y -= bullet_speed * dt
        pygame.draw.circle(screen, "red", bullet_pos, 5)

    bullet_count = 0
    for bullet in bullets:
        bullet_count += 1

    counter += 1
    if counter == 180:
        enemies.append(pygame.Vector2(random.randint(0, screen_width), 0))
        counter = 0

    enemy_count = 0
    for enemy in enemies:
        enemy.y += 100 * dt
        pygame.draw.circle(screen, "green", enemy, 20)
        enemy_count += 1

    enemies = [enemy for enemy in enemies if enemy.y < screen_height]
    
    if len(enemies) > 0 and pygame.Vector2(player_pos.x, player_pos.y).distance_to(pygame.Vector2(enemies[0].x, enemies[0].y)) < 50:
        running = False

    current_frame += 1
    if target_frame == current_frame:
        print(f'Bullets in scene: {bullet_count}')
        print(f'Enemies in scene: {enemy_count}')
        current_frame = 0
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()



