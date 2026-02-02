import random
import time
import math
import pygame
pygame.init()

width, height = 800, 600
timer = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Train")
target_event = pygame.USEREVENT
target_padding = 20

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
            self.grow = False
        
        if self.grow:
            self.size += self.growth_rate
        else:
            self.size -= self.growth_rate
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), int(self.size))
        pygame.draw.circle(window, self.secondary_color, (self.x, self.y), int(self.size * 0.8))
        pygame.draw.circle(window, self.color, (self.x, self.y), int(self.size * 0.6))
        pygame.draw.circle(window, self.secondary_color, (self.x, self.y), int(self.size * 0.4))

def draw_hitboxes(window, hitboxes):
    window.fill("black")
    for hitbox in hitboxes:
        hitbox.draw(window)
    pygame.display.update()
def main():
    playing = True
    hitboxes = []
    frames = pygame.time.Clock()
    pygame.time.set_timer(target_event, timer)
    while playing:
        frames.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break
            if event.type == target_event:
                x = random.randint(target_padding,width-target_padding)
                y = random.randint(target_padding,
                height-target_padding)
                hitbox = Target(x,y)
                hitboxes.append(hitbox)
        for hitbox in hitboxes:
            hitbox.update()
        draw_hitboxes(window, hitboxes)

    pygame.quit()


if __name__ == "__main__":
    main()