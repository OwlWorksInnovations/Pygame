import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

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
    pygame.draw.rect(screen, "white", pygame.Rect(100, 100, 50, 150))
    pygame.draw.rect(screen, "white", pygame.Rect(1100, 100, 50, 150))
    # Render game above

    pygame.display.flip()

pygame.quit()

