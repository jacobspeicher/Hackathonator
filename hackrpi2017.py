
import asyncio
from graphics import *


def main():
    win = GraphWin('Hackathonator', 800, 600)
    win.setBackground(color_rgb(34, 40, 49))

    head = Circle(Point(win.getWidth()/2, win.getHeight()), 100)
    head.setFill('yellow')
    head.draw(win)

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

    win.getMouse()
    win.close()




if __name__=='__main__':
    main()
