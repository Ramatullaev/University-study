# import pygame
# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# done = True
# clock = pygame.time.Clock()
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done == False
#         if event.type == pygame.KEYDOWN:
#             pressed = pygame.key.get_pressed()
#             if pressed[pygame.K_UP]: y -= 3
#             if pressed[pygame.K_DOWN]: y += 3
#             if pressed[pygame.K_LEFT]: x -= 3
#             if pressed[pygame.K_RIGHT]: x += 3

#     screen.fill((255, 255, 255))
#     pygame.draw.circle(screen, (255, 0, 0), (200, 150), 25)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

x = 200
y = 150

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                y -= 3
            if pressed[pygame.K_DOWN]:
                y += 3
            if pressed[pygame.K_LEFT]:
                x -= 3
            if pressed[pygame.K_RIGHT]:
                x += 3

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
