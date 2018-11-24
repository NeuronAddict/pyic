import sys
import time

l = 100
s = '.' * 100

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def update(str_, newline_count):
    if len(s) != l:
        raise Exception("Length error : " + str_)
    time.sleep(1.5)

    delete_last_lines(newline_count + 1)
    sys.stdout.write(str_ + '\n')
    sys.stdout.flush()

sys.stdout.write(s)
sys.stdout.flush()


s = 'A' * 20 + '.' * 30  + '\n' + '.' * 49
update(s, 0)

s = 'A' * 20 + '\n' + 'B' * 29 + '\n' + '.' * 49
update(s, 1)

s = 'A' * 20 + '\n' + 'B' * 29 + '\n' + 'A' * 20 + '\n' + 'C' * 27 + '\n'
update(s, 2)


print('\n\n\n' + s)



def bk():
    sys.stdout.write('0 %')
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write('\r{}  %'.format(i))
        sys.stdout.flush()
    print('Done!')
