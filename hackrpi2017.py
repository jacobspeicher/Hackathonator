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

    string = ''
    wrong_string = ''
    font = pygame.font.Font('RobotoMono-Medium.ttf', 12)
    code_line = 'I may be slow but watch me go'
    code_index = 0
    line_height = 40
    finished_lines = []
    mods = [304, 303, 13, 301]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key != pygame.K_BACKSPACE:
                    hand = random.randint(0,1)
                    if hand == 0:
                        sprites['l_hand'].move()
                    else:
                        sprites['r_hand'].move()
                    if event.unicode == code_line[code_index] and len(string) == len(wrong_string):
                        string += event.unicode
                        wrong_string += event.unicode
                        code_index += 1
                        if code_index == len(code_line):
                            finished_lines.append((string, line_height))
                            code_line = "This time it's personal"
                            string = ''
                            wrong_string = ''
                            code_index = 0
                            line_height += 15
                    else:
                        if event.key not in mods and len(string) == len(wrong_string):
                            if code_line[code_index] == ' ':
                                wrong_string += '_'
                            else:
                                wrong_string += code_line[code_index]
                            code_index += 1
                else:
                    if(code_index > 0):
                        if len(string) == len(wrong_string):
                            string = string[:-1]
                        wrong_string = wrong_string[:-1]
                        code_index -= 1
                        sprites['r_hand'].move()

        for sprite_name, sprite in sprites.items():
            sprite.update()

        win.fill((0, 0, 0))
        screen_bezel = pygame.draw.rect(win, (255, 255, 255), (30, 10, 740, 530))
        screen = pygame.draw.rect(win, (34, 40, 49), (50, 30, 700, 490))
        camera = pygame.draw.circle(win, (0, 0, 0), (width//2, 20), 5)
        head = pygame.draw.circle(win, (255,255,0), (width//2, height), 100)
        code = font.render(code_line, 1, (255, 255, 255))
        wrong_text = font.render(wrong_string, 1, (255, 255, 255), (255, 0, 0))
        text = font.render(string, 1, (253, 112, 20), (34, 40, 49))

        for line in finished_lines:
            f_line = font.render(line[0], 1, (253, 112, 20))
            win.blit(f_line, (55, line[1])) 

        win.blit(code, (55, line_height))
        win.blit(wrong_text, (55, line_height))
        win.blit(text, (55, line_height))
        head = pygame.draw.circle(win, (255,255,0), (width//2, height), 100)
        for sprite_name, sprite in sprites.items():
            sprite.draw(win)

        pygame.display.flip()
        my_clock.tick(60)

    pygame.quit()


if __name__=='__main__':
    main()
