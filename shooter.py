import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Shooter")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_img = pygame.Surface((50, 50))
player_img.fill(WHITE)
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 60))

# Bullet
bullet_img = pygame.Surface((5, 20))
bullet_img.fill(RED)
bullets = []

# Enemy
enemy_img = pygame.Surface((40, 40))
enemy_img.fill((0, 255, 0))
enemies = []

# Game loop
running = True
score = 0
font = pygame.font.SysFont(None, 36)

def spawn_enemy():
    x = random.randint(0, WIDTH - 40)
    rect = enemy_img.get_rect(topleft=(x, -40))
    enemies.append(rect)

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit bullets
            bullet_rect = bullet_img.get_rect(midbottom=player_rect.midtop)
            bullets.append(bullet_rect)

    # Update bullets
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, 30) == 1:
        spawn_enemy()

    # Update enemies
    for enemy in enemies[:]:
        enemy.y += 3
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

    # Collision
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    # Draw
    screen.blit(player_img, player_rect)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
