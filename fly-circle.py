import pygame
import sys

class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y


if __name__ == "__main__":
    circle = Circle(10, 100, 100)
    pygame.init()


    window_width = 500
    window_height = 400
    circle.radius = 15


    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("This circle is bouncing")


    circle = Circle(circle.radius, window_width // 2, window_height // 2)

    vx = 10
    vy = 12
    clock = pygame.time.Clock()


    moving = True
    while moving:

        for i in pygame.event.get(): #
            if i.type == pygame.QUIT:
                moving = False



        screen.fill((0, 30, 0))  # Black background


        circle.move(vx, vy)


        if circle.x - circle.radius < 0 or circle.x + circle.radius > window_width:
            vx = -vx
        if circle.y - circle.radius < 0 or circle.y + circle.radius > window_height:
            vy = -vy


        circle.draw(screen, (255, 0, 0))  

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()
