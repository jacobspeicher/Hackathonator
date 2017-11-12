import pygame
import random


code_lines = [
    'for slice in pizza:',
    'print("Self Destructing ...")',
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
    '(\x.y (\x.(x x) \x.(x x)))',
    'for fname in [x.filename for x in totalzip.filelist]:',
    'hs_mains_histogram[len(mains)] = hs_mains_histogram.get(len(mains), 0) + 1',
    'sub = subprocess.Popen([os.getenv(\'HOME\')+\'/alpha_equivalent\', theirs, ours], stdout=subprocess.PIPE)',
    'print(\'Error for %r: %r\' % (peoplenames, stderr_log))',
    'variance = lambda xs: average(map(lambda x: x**2, xs)) - average(xs)**2',
    'case {Pri, Sender} of',
    '{X, true} when X =< 0 ->',
    'Sender ! {reply, LBit, InitTTL, Timestamp, LR},',
    'Pids = lists:map(fun({ID, Host, Node, Priority, Tolerance}) ->',
    'binary_to_list(Address),',
    '[Col | columns(<<>>, Rest)];',
    'let seq e1 e2 = (\z ->  e2) e1',
    'productList = foldr (*) 1',
    'binmap b (h1:t1) (h2:t2) = (b h1 h2):(binmap b t1 t2)',
    'infSqrs = map (\x -> 2^x) [0..]',
    'lp2pl = foldr (\(x,y) (xl,yl) -> (x:xl,y:yl)) ([],[])',
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
    'if self.fit == Fit.Next and self.recent_loc+proc.mem <= part_loc+part_len and self.recent_loc > part_loc:',
    'self.eq.put((timestamp+proc.get_burst_len(timestamp-self.total_time_added), Event.proc_exit, proc))',
    'proc.pos.append((part[0], used_mem))',
    'num_bursts = len(split)-2',
    'mem = Memory(Fit.Next, eq, procs)',
    'while not self.queue.empty() and popped[-1][2] != process:',
    'if event == Event.arrival:',
    'if process.num_bursts-process.used_bursts > 1:',
    'if self.algo == Algo.SRT and self.busy and self.running_process is not None and process.remaining_time < rt:',
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
    font = pygame.font.Font(None, 16)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                hand = random.randint(0,1)
                if hand == 0:
                    sprites['l_hand'].move()
                else:
                    sprites['r_hand'].move()
                string += event.unicode

        # game logic
        for sprite_name, sprite in sprites.items():
            sprite.update()

        # game render
        win.fill((0, 0, 0))
        screen_bezel = pygame.draw.rect(win, (255, 255, 255), (30, 10, 740, 530))
        screen = pygame.draw.rect(win, (34, 40, 49), (50, 30, 700, 490))
        camera = pygame.draw.circle(win, (0, 0, 0), (width//2, 20), 5)
        head = pygame.draw.circle(win, (255,255,0), (width//2, height), 100)
        text = font.render(string, 1, (253, 112, 20))
        win.blit(text, (0, 0))
        head = pygame.draw.circle(win, (255,255,0), (width//2, height), 100)
        for sprite_name, sprite in sprites.items():
            sprite.draw(win)

        pygame.display.flip()
        my_clock.tick(60)

    pygame.quit()


if __name__=='__main__':
    main()
