import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Car Game")

# Set up the car
car_image = pygame.image.load("car.png")
car_width = 50
car_height = 100
car_x = (window_width - car_width) // 2
car_y = window_height - car_height - 10

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render the game
    window.fill((255, 255, 255))  # Fill the window with white color
    window.blit(car_image, (car_x, car_y))  # Draw the car on the window

    pygame.display.update()

# Quit the game
pygame.quit()
