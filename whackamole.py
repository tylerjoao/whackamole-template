import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_position = [0, 0]
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_rect = mole_image.get_rect(topleft=mole_positiont)
                    if mole_rect.collidepoint(event.pos):
                        mole_position[0] = random.randrange(21) * 32
                        mole_position[1] = random.randrange(17) * 32
            screen.fill("light green")
            for i in range(21):
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))
            for i in range(17):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
