import random
import time
import math
import pygame
pygame.init()

width, height = 800, 600
sc_height = 40
timer = 400
hp = 5
font = pygame.font.SysFont("Arial", 16)

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

def format_time(sec):
    m = int(sec) // 60
    s = int(sec) % 60
    return f"{m:02}:{s:02}"
def scorecard(window, elapsed_t, score, miss):
    pygame.draw.rect(window, "#1e293b", (0,0, width, sc_height))
    sc_time = font.render(f"Time: {format_time(elapsed_t)}", 1, "#b7c9d4")

    sc_score = font.render(f"Score: {score}", 1, "#b7c9d4")
    sc_hp = font.render(f"HP: {hp-miss}", 1, "#b7c9d4")

    window.blit(sc_time, (5,5))
    window.blit(sc_score, (200,5))
    window.blit(sc_hp, (400,5))
def draw_hitboxes(window, hitboxes):
    window.fill("#020617")
    for hitbox in hitboxes:
        hitbox.draw(window)


def game_over_screen(window, score, clicks, elapsed_t):
    window.fill("#0f172a")
    title_font = pygame.font.SysFont("Arial", 48, bold=True)
    info_font = pygame.font.SysFont("Arial", 22)
    title = title_font.render("GAME OVER", True, "#e5e7eb")
    score_text = info_font.render(f"Score: {score}", True, "#cbd5f5")
    acc = round((score / clicks) * 100,1) if clicks else 0
    accuracy = info_font.render(f"Accuracy: {acc}%", True, "#cbd5f5")
    time_text = info_font.render(
    f"Time: {format_time(elapsed_t)}", True, "#cbd5f5")
    exit_text = info_font.render("Press ESC to quit", True, "#94a3b8")

    window.blit(title, (width // 2 - title.get_width() // 2, 180))
    window.blit(score_text, (width // 2 - score_text.get_width() // 2, 260))
    window.blit(accuracy, (width // 2 - accuracy.get_width() // 2, 295))
    window.blit(time_text, (width // 2 - time_text.get_width() // 2, 330))
    window.blit(exit_text, (width // 2 - exit_text.get_width() // 2, 380))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting = False
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
        time_elapse = time.time() - start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break
            if event.type == target_event:
                x = random.randint(target_padding,width-target_padding)
                y = random.randint(sc_height + target_padding,
                height-target_padding)
                hitbox = Target(x,y)
                hitboxes.append(hitbox)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for hitbox in hitboxes[:]:
            hitbox.update_size()
            if hitbox.size <= 0:
                hitboxes.remove(hitbox)
                miss += 1
            
            if click and hitbox.hitbox_hit(mouse_position[0], mouse_position[1]):
                hitboxes.remove(hitbox)
                score += 1
        if miss >= hp:
            game_over_screen(window, score, clicks, time_elapse)
            playing = False
        draw_hitboxes(window, hitboxes)
        scorecard(window, time_elapse, score, miss)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()