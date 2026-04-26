import pygame
from pygame import draw, display

# Set up pygame window
pygame.init()
window = display.set_mode((600, 600))
display.set_caption("A Very Big House")
window.fill("cyan")

# set up objects

background = pygame.Rect(0, 220, 600, 400)
house = pygame.Rect(90,180, 300, 300)
door = pygame.Rect(190, 315, 100, 140)
window1 = pygame.Rect(110, 215, 60, 60)
window2 = pygame.Rect(310, 215, 60, 60)
window1_1 = pygame.Rect(110, 215, 30, 60)
window1_2 = pygame.Rect(310, 215, 30, 60)
doorKnob = pygame.Rect(265, 384, 15, 5)
roof=[(80,180), (240,100), (400,180)]

#draw house objects

draw.rect(window, "green", background)
draw.rect(window, "light grey", house)
draw.rect(window, "orangered", door)
draw.rect(window, "black", window1)
draw.rect(window, "white", window2)
draw.rect(window, "dark grey", doorKnob)
draw.rect(window, "white", window1_1)
draw.rect(window, "black", window1_2)
draw.polygon(window, "brown", roof)
display.flip()

#update display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ✅ handles close button
            running = False

pygame.quit()
