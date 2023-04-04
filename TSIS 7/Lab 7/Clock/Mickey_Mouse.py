import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((820,820))
image = pygame.image.load("/Users/snezhok/Desktop/PP2/TSIS 7/Lab 7/Clock/bb.png")
second_hand = pygame.image.load("/Users/snezhok/Desktop/PP2/TSIS 7/Lab 7/Clock/second.png")
angle = 90
while True:
    screen.blit(image,(0,0))
    rotated_sec = pygame.transform.rotate(second_hand, angle)
    rotated_sec_rect = rotated_sec.get_rect(center = (410, 410))
    screen.blit(rotated_sec, rotated_sec_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    angle -= 1/6
    pygame.display.update()
    clock.tick(60)


