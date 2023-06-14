import pygame
import random
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
i = 0
velocity = 15
# Set the height and width of the screen
SIZE = [1920, 1080]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
	i = random.randrange(0, 100)
 
	for event in pygame.event.get():   # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True   # Flag that we are done so we exit this loop

	# Set the screen background
	screen.fill(BLACK)
	if i < 10 and i > 0:
		for e in range(15):	
			x = random.randrange(0, 1920)
			y = random.randrange(0,10)
			snow_list.append([x, y])
	# Process each snow flake in the list
	for i in range(len(snow_list)):

		# Draw the snow flake
		image = pygame.draw.circle(screen, WHITE, snow_list[i], 15)

		# Move the snow flake down one pixel
		snow_list[i][1] += 1*velocity

		# If the snow flake has moved off the bottom of the screen
			
 
    # Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	clock.tick(60)

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.