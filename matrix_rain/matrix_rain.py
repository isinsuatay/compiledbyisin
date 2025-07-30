import pygame
import random
import sys

class MatrixRain:
    def __init__(self, width=1280, height=720, font_size=18):
        pygame.init()
        self.width = width
        self.height = height
        self.font_size = font_size

        self.font = pygame.font.Font("./fonts/NotoSansJP-VariableFont_wght.ttf", self.font_size)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Matrix Rain - Cinematic")
        self.clock = pygame.time.Clock()

        self.chars = "アイウエオカキクケコサシスセソ023456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.columns = self.width // self.font_size
        self.rows = self.height // self.font_size
        self.drops = [random.randint(0, self.rows) for _ in range(self.columns)]
        self.column_chars = [random.choice(self.chars) for _ in range(self.columns)]

        # Renk geçişi
        self.trail_colors = [
            (255, 255, 255),   
            (0, 255, 70),
            (0, 200, 50),
            (0, 150, 30),
            (0, 100, 20),
            (0, 80, 10),
            (0, 50, 5)         
        ]

    def draw(self):
       
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 20, 0, 20))  
        self.screen.blit(overlay, (0, 0))

        for i in range(self.columns):
            x = i * self.font_size
            y = self.drops[i] * self.font_size

            char = self.column_chars[i]

            head_color = self.trail_colors[0]
            head_text = self.font.render(char, True, head_color)
            self.screen.blit(head_text, (x, y))

            for j, color in enumerate(self.trail_colors[1:], start=1):
                trail_y = y - j * self.font_size
                if trail_y < 0:
                    break
                trail_text = self.font.render(char, True, color)
                self.screen.blit(trail_text, (x, trail_y))

            self.drops[i] += 1
            if self.drops[i] * self.font_size > self.height or random.random() > 0.975:
                self.drops[i] = 0
                self.column_chars[i] = random.choice(self.chars)

    def run(self):
        while True:
            self.draw()
            pygame.display.flip()
            self.clock.tick(20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    MatrixRain().run()