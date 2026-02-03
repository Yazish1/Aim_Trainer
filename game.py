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
    
    def update_size(self):
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

    def hitbox_hit(self, x, y):
        distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        if distance <= self.size:
            return True
        else:
            return False

def draw_hitboxes(window, hitboxes):
    window.fill("black")
    for hitbox in hitboxes:
        hitbox.draw(window)
    pygame.display.update()
def main():
    playing = True
    hitboxes = []
    frames = pygame.time.Clock()

    # For user
    score = 0
    clicks = 0
    start = time.time()
    miss = 0

    pygame.time.set_timer(target_event, timer)
    
    while playing:
        frames.tick(60)
        click = False
        mouse_position = pygame.mouse.get_pos()
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for hitbox in hitboxes:
            hitbox.update_size()
            if hitbox.size <= 0:
                hitboxes.remove(hitbox)
                miss += 1
            
            if click and hitbox.hitbox_hit(mouse_position[0], mouse_position[1]):
                hitboxes.remove(hitbox)
                score += 1
        draw_hitboxes(window, hitboxes)

    pygame.quit()


if __name__ == "__main__":
    main()