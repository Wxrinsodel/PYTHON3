import pygame
import sys
import random

class Circle:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y


window_width = 500
window_height = 400


pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bouncing Circles")


bg_color = (37, 150, 190)


num_circles = 20
circles = []
velocities = []

for _ in range(num_circles):
    radius = random.randint(10, 20)
    x = random.randint(radius, window_width - radius)
    y = random.randint(radius, window_height - radius)
    color = (0,0,0)
    circles.append(Circle(radius, x, y, color))
    velocities.append((random.choice([-7, 5]), random.choice([-7, 5])))


clock = pygame.time.Clock()
moving = True


while moving:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            moving = False

    screen.fill(bg_color)


    #Just want to organize vx, vy

    for i, circle in enumerate(circles):
        vx, vy = velocities[i]
        circle.move(vx, vy)

        if circle.x - circle.radius < 0 or circle.x + circle.radius > window_width:
            velocities[i] = (-vx, vy)
        if circle.y - circle.radius < 0 or circle.y + circle.radius > window_height:
            velocities[i] = (vx, -vy)

        circle.draw(screen)

    
    pygame.display.flip()
    clock.tick(30)


pygame.quit()
sys.exit()
