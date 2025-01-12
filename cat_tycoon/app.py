import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_speed = 1000

money = 20
happiness = 50

can_add_money = time.time()
add_money_delay = 1
multiplier = 1
price = 25

class Button:
    def __init__(self, text, x, y, width, height, text_color, button_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.button_color = button_color

    def render(self, screen):
        pygame.draw.rect(screen, self.button_color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return (self.x < mouse_pos[0] < self.x + self.width and
                self.y < mouse_pos[1] < self.y + self.height)

    def is_clicked(self, mouse_pos):
        return self.is_hovered(mouse_pos) and pygame.mouse.get_pressed()[0]

while running:
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Render game here

    # Cat
    pygame.draw.circle(screen, "white", (screen.get_width() / 2, screen.get_height() / 2), 40)

    # Button
    add_money_btn = Button("Buy Cat Food", 100, 50, 200, 50, "black", "white")
    add_money_btn.render(screen)
    if add_money_btn.is_clicked(pygame.mouse.get_pos()) and time.time() > can_add_money:
        can_add_money = time.time() + add_money_delay
        money += 1 * multiplier

    upgrade_btn = Button("Upgrade Cat", 100, 150, 200, 50, "black", "white")
    upgrade_btn.render(screen)
    if upgrade_btn.is_clicked(pygame.mouse.get_pos()) and money >= price:
        money -= price
        multiplier += 1
        price *= multiplier

    play_btn = Button("Play With Cat", 100, 250, 200, 50, "black", "white")
    play_btn.render(screen)
    if play_btn.is_clicked(pygame.mouse.get_pos()) and happiness < 100:
        happiness += 10

    # Labels
    # Money
    money_text = str(money)
    money_text_surface = pygame.font.Font(None, 36).render(money_text, True, "white")
    screen.blit(money_text_surface, (100, 650))
    # Energy
    # Health
    # Hunger
    # Render game above
    pygame.display.flip()

    # Add money over time
    if time.time() > can_add_money:
        can_add_money = time.time() + add_money_delay
        money += 1 * multiplier

    # Decrease happiness over time
    if time.time() % 1 < 0.5:
        happiness -= 0.1
    else:
        happiness += 0.1
    happiness = max(0, min(happiness, 100))

running = False


