import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def delete_last_lines(n=1):
    sys.stdout.write((CURSOR_UP_ONE + ERASE_LINE) * n)
    sys.stdout.flush()


def update_screen(old_str, new_str):
    delete_last_lines(old_str.count('\n') + 1)
    print(new_str)
