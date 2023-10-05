import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Make a peggle like game 

#1 show the screen

#2 make the ball you shoot

#3 make the balls collides with and have them spawn in random places

#4 make specil balls that when collided it gives a power 

#5 special balls with different abilities

# could make upgrades such as more force, give the player coins based
# on how mnay pegs hit

# the player can buy and upgrade the shooting ball