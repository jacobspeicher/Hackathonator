import pygame

def main():
    pygame.init()
    width = 800
    height = 600
    win = pygame.display.set_mode((width,height))
    win.fill((0, 0, 0))

    screen_bezel = pygame.draw.rect(win, (255, 255, 255), (30, 10, 740, 530))
    screen = pygame.draw.rect(win, (34, 40, 49), (50, 30, 700, 490))
    camera = pygame.draw.circle(win, (0, 0, 0), (width//2, 20), 5)
    head = pygame.draw.circle(win, (255,255,0), (width//2, height), 100)

    string = ''
    font = pygame.font.Font(None, 16)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                string += event.unicode

        text = font.render(string, 1, (253, 112, 20))
        win.blit(text, (0, 0))


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

'''
    left_hand = Circle(Point(win.getWidth()/2 - 140, win.getHeight()), 20)
    left_hand.setFill('yellow')
    left_hand.draw(win)
    right_hand = Circle(Point(win.getWidth()/2 + 140, win.getHeight()), 20)
    right_hand.setFill('yellow')
    right_hand.draw(win)

    def move_l_hand_back():
        left_hand.move(5, 20)
    def move_r_hand_back():
        right_hand.move(-5, 20)


    left_or_right = True
    try:
        while True:
            key = win.getKey()
            if left_or_right:
                left_hand.move(-5, -20)
            else:
                right_hand.move(5, -20)
            left_or_right = not left_or_right
    except GraphicsError:
        pass

'''




if __name__=='__main__':
    main()
