import pygame
pygame.init()

width, height = 800, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Train")

class Target:
    maximum_size = 30
    growth_rate = 0.2
    color = "red"
    secondary_color = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    

    def update(self):
        if self.size + self.growth_rate >= self.maximum_size:
            self.gorw = False
        
        if self.grow:
            self.size += self.growth_rate
        else:
            self.size -= self.growth_rate
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)
        pygame.draw.circle(window, self.secondary_color, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(window, self.secondary_color, (self.x, self.y), self.size * 0.4)