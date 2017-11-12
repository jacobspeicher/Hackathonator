
import pygame
import random


class HandSprite(object):

    def __init__(self, color, pos, radius):
        self.color = color
        self.init_pos = pos
        self.pos = pos
        self.radius = radius
        self.animation_time = 0
        self.animation_length = 10

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def update(self):
        if self.animation_time > 0:
            self.animation_time = self.animation_time + 1
            if self.animation_time > self.animation_length:
                self.pos = self.init_pos
                self.animation_time = 0

    def move(self):
        if self.animation_time == 0:
            self.pos = (self.init_pos[0], self.init_pos[1] - 20)
            self.animation_time = 1


def main():
    pygame.init()
    width = 800
    height = 600
    win = pygame.display.set_mode((width,height))

    sprites = dict()
    sprites['l_hand'] = HandSprite((255,255,0), (width//2 -140, height), 20)
    sprites['r_hand'] = HandSprite((255,255,0), (width//2 +140, height), 20)

    my_clock = pygame.time.Clock()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.KEYDOWN:
            hand = random.randint(0,1)
            if hand == 0:
                sprites['l_hand'].move()
            else:
                sprites['r_hand'].move()

        win.fill((34, 40, 49))

        for sprite_name, sprite in sprites.items():
            sprite.update()

        head = pygame.draw.circle(win, (255,255,0), (width//2, height), 100)
        for sprite_name, sprite in sprites.items():
            sprite.draw(win)

        pygame.display.flip()
        my_clock.tick(60)

    pygame.quit()


if __name__=='__main__':
    main()
