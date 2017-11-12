#!/usr/bin/python3
# hackrpi2017.py by Jacob Speicher and Greg Cowan

import argparse
import operator
import os
import pygame
import random
import socket


code_lines = [
    'for slice in pizza:',
    'print("Self Destructing...")',
    'i++',
    'class Sound(object):',
    'width = 800',
    'self.pos[0] += self.vel[0]',
    'sleep(999999999)',
    'if params is not None:',
    'curl("https://straightape.com", type="POST")',
    'Play.objects.create(author="Margaret Edson", title="W;t")',
    'self.radius = PI*r',
    'nextChars c = dropWhile (<= c) (cycle [\'a\'..\'z\'])',
    '(\\x.y (\\x.(x x) \\x.(x x)))',
    'for fname in [x.filename for x in totalzip.filelist]:',
    'hs_mains_histogram[len(mains)] = hs_mains_histogram.get(len(mains), 0) + 1',
    'sub = subprocess.Popen([os.getenv(\'HOME\'), theirs, ours], stdout=subprocess.PIPE)',
    'print(\'Error for %r: %r\' % (peoplenames, stderr_log))',
    'variance = lambda xs: average(map(lambda x: x**2, xs)) - average(xs)**2',
    'case {Pri, Sender} of',
    '{X, true} when X =< 0 ->',
    'Sender ! {reply, LBit, InitTTL, Timestamp, LR},',
    'Pids = lists:map(fun({ID, Host, Node, Priority, Tolerance}) ->',
    'binary_to_list(Address),',
    '[Col | columns(<<>>, Rest)];',
    'let seq e1 e2 = (\\z ->  e2) e1',
    'productList = foldr (*) 1',
    'binmap b (h1:t1) (h2:t2) = (b h1 h2):(binmap b t1 t2)',
    'infSqrs = map (\\x -> 2^x) [0..]',
    'lp2pl = foldr (\\(x,y) (xl,yl) -> (x:xl,y:yl)) ([],[])',
    'z_trans = order_trans(order, x1(i,j), x2(i,j));',
    'H = Z*inverse(transpose(Z)*Z + lambda*eye(45,45))*transpose(Z);',
    'y_test = sign(dot(w_reg, Z_test(j,:)));',
    'inv = grayscale(i*w+(w-j+1));',
    'scatter(red_x, red_y, [], \'r\', \'x\', \'LineWidth\', 1.0)',
    'self.mem = proc_mem',
    'class Event(enum.Enum):',
    'if loc+part_len < self.recent_loc:',
    'self.freed.insert(index, (loc+length, part_len-length))',
    'self.mem = self.mem[0:loc] + char*length + self.mem[loc+length:]',
    'if self.fit == Fit.Next and self.loc+proc.mem <= part_loc+part_len and self.loc > part_loc:',
    'self.eq.put((time+proc.get_burst_len(timestamp-self.total_time_added), Event.proc_exit, proc))',
    'proc.pos.append((part[0], used_mem))',
    'num_bursts = len(split)-2',
    'mem = Memory(Fit.Next, eq, procs)',
    'while not self.queue.empty() and popped[-1][2] != process:',
    'if event == Event.arrival:',
    'if process.num_bursts-process.used_bursts > 1:',
    'if self.algo == Algo.SRT and self.busy and self.running_process is not None and process.rem_time',
    'else:',
    'def parse_input(filename):',
]


class HandSprite(object):

    def __init__(self, color, pos, radius):
        self.color = color
        self.init_pos = pos
        self.pos = pos
        self.radius = radius
        self.animation_time = 0
        self.animation_length = 20

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


white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)
red = (255,0,0)
orange = (253, 112, 20)
gray = (34, 40, 49)


def main():
    parser = argparse.ArgumentParser(description='Hackathonator. Type faster than your friends!')
    parser.add_argument('-n', dest='hostname', type=str, help='Hostname of opponent who is running as a server.')
    parser.add_argument('-p', dest='port', type=int, help='Port of opponent who is running as a server.', default=9876)
    args = parser.parse_args()

    pygame.init()
    width = 1200
    height = 720
    win = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Hackathonator')

    user = os.environ['USER']

    sprites = dict()
    sprites['l_hand'] = HandSprite(yellow, (width//2 -140, height), 20)
    sprites['r_hand'] = HandSprite(yellow, (width//2 +140, height), 20)

    my_clock = pygame.time.Clock()

    string = ''
    wrong_string = ''
    font = pygame.font.Font('RobotoMono-Medium.ttf', 14)
    code_line = 'I may be slow but watch me go'
    code_index = 0
    line_height = 40
    finished_lines = []
    mods = [304, 303, 13, 301]

    connections = []
    opponents = dict()
    TIMEOUT = 0.001
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    is_server = None
    if args.hostname is None:
        is_server = True
        HOST = ''
        PORT = 9876
        sock.bind((HOST, PORT))
        sock.listen(8)
    else:
        is_sever = False
        sock.connect((args.hostname, args.port))
    sock.settimeout(TIMEOUT)

    try:
        while True:
            # Event handling and game logic
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

                        if code_index < len(code_line):
                            if (event.unicode == code_line[code_index] and len(string) == len(wrong_string)) or event.key == pygame.K_LALT:
                                string += event.unicode
                                wrong_string += event.unicode
                                code_index += 1
                                if code_index == len(code_line) or event.key == pygame.K_LALT:
                                    finished_lines.append((code_line, len(finished_lines)+1))
                                    code_line = code_lines[random.randint(0,len(code_lines)-1)]
                                    string = ''
                                    wrong_string = ''
                                    code_index = 0
                                    reply_str = user + ',' + str(len(finished_lines))
                                    if is_server:
                                        for conn in connections:
                                            conn.sendall(bytearray(reply_str, 'utf-8'))
                                    else:
                                        try:
                                            sock.sendall(bytearray(reply_str, 'utf-8'))
                                        except socket.error:
                                            pass
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

            # Networking
            if is_server:
                try:
                    conn, addr = sock.accept()
                    conn.settimeout(TIMEOUT)
                    connections.append(conn)
                    print(conn)
                except socket.timeout:
                    try:
                        new_conns = []
                        for conn in connections:
                            msg = conn.recv(256)
                            if msg is not None and msg != b'':
                                msg = str(msg).strip('b').strip('\'')
                                sender, s_line = msg.split(',')
                                opponents[sender] = s_line
                                print(msg)
                                new_conns.append(conn)
                            else:
                                conn.close()
                        connections = new_conns
                    except socket.timeout:
                        pass
            else:
                try:
                    msg = sock.recv(256)
                    if msg is not None and msg != b'':
                        msg = str(msg).strip('b').strip('\'')
                        sender, s_line = msg.split(',')
                        opponents[sender] = s_line
                        print(msg)
                    else:
                        sock.close()
                except socket.timeout:
                    pass
                except socket.error:
                    pass

            # Rendering
            win.fill((0, 0, 0))
            screen_bezel = pygame.draw.rect(win, white, (30, 10, width - 60, height - 70))
            screen = pygame.draw.rect(win, gray, (50, 30, width - 100, height - 110))
            camera = pygame.draw.circle(win, black, (width//2, 20), 5)
            head = pygame.draw.circle(win, yellow, (width//2, height), 100)
            
            if code_index != len(code_line):
                cursor = font.render(code_line[code_index], 1, black, white)

            code = font.render(code_line, 1, white)
            wrong_text = font.render(wrong_string, 1, white, red)
            text = font.render(string, 1, orange, gray)
            l_num = font.render(str(len(finished_lines) + 1) + '.', 1, white)

            line_h = line_height
            for line in finished_lines[-38:]:
                f_line = font.render(line[0], 1, orange)
                win.blit(f_line, (55 + font.size(str(line[1]) + '. ')[0], line_h)) 
                l_number = font.render(str(line[1]) + '. ', 1, white)
                win.blit(l_number, (55, line_h))
                line_h = min(line_h+15, 625)

            start_line_x = font.size(str(len(finished_lines) + 1) + '. ')[0]
            win.blit(code, (55 + start_line_x, line_h))
            win.blit(cursor, (55 + start_line_x  + (font.size(string)[0]), line_h))
            win.blit(wrong_text, (55 + start_line_x, line_h))
            win.blit(text, (55 + start_line_x, line_h))
            win.blit(l_num, (55, line_h))

            head = pygame.draw.circle(win, yellow, (width//2, height), 100)
            for sprite_name, sprite in sprites.items():
                sprite.draw(win)

            sorted_opps = sorted(opponents.items(), key=operator.itemgetter(1), reverse=True)
            if len(sorted_opps) != 0:
                opp = sorted_opps[0]
                opponent = font.render(opp[0] + ": " + opp[1], 1, white)
                win.blit(opponent, (55, height-20))

            pygame.display.flip()
            my_clock.tick(240)

    except pygame.error:
        pass

    pygame.quit()
    sock.close()


if __name__=='__main__':
    main()
