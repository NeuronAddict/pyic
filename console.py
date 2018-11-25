import sys
import time

l = 100
s = '.' * 100

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def delete_last_lines(n=1):
    sys.stdout.write((CURSOR_UP_ONE + ERASE_LINE) * n)
    sys.stdout.flush()


def test():
    print('.' * 100)
    time.sleep(.5)
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    print('A' * 49 + '\n' + '.' * 50)
    time.sleep(.5)
    print((CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE) * 2)
    print('A' * 49 + '\n' + 'B' * 49 + '\n')



CURSOR_UP_ONE = '\x1b[1A'  # <--Replace with '\033[F' if you don't have VT100
ERASE_LINE = '\x1b[2K'  # <--Replace with '\033[K' if you don't have VT100

def close_garage_dors():
    a = '_ _ _'
    for i in range(5):
        time.sleep(.5)
        print(a)
    for b in range(5):
        time.sleep(.5)
        print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

#close_garage_dors()


def update_screen(old_str, new_str):
    delete_last_lines(old_str.count('\n') + 1)
    print(new_str)


s0 = 'A' * 20 + '.' * 30 + '\n' + '.' * 49
s1 = 'A' * 20 + '\n' + 'B' * 29 + '\n' + '.' * 49
s2 = 'A' * 20 + '\n' + 'B' * 29 + '\n' + 'A' * 20 + '\n' + '.' * 27 + '\n'
s3 = 'A' * 20 + '\n' + 'B' * 29 + '\n' + 'A' * 20 + '\n' + 'C' * 27 + '\n'
print(s0)
time.sleep(1)
update_screen(s0, s1)
time.sleep(1)
update_screen(s1, s2)
time.sleep(1)
update_screen(s2, s3)

#print('\n\n\n' + s2)



def bk():
    sys.stdout.write('0 %')
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write('\r{}  %'.format(i))
        sys.stdout.flush()
    print('Done!')
