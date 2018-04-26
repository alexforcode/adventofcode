'''http://adventofcode.com/2017/day/3'''
from itertools import count


def sum_spiral():
    '''
    Fill the spiral with values.
    Yield each value to compare.
    '''
    loc, x, y = {(0, 0): 1}, 0, 0
    for step in count(1, 2):
        for (ds, dx, dy) in [(0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)]:
            for _ in range(step + ds):
                x += dx
                y += dy
                loc[x, y] = sum(loc.get((k, l), 0) for k in range(x - 1, x + 2) for l in range(y - 1, y + 2))
                yield loc[x, y]


def find_first_largest_value(num):
    '''
    Return first value that is larger than num
    '''
    for val in sum_spiral():
        if val > num:
            return val


def test(func):
    '''Test function'''
    print('Test: find_first_largest_value function.')

    print('#1: ', end='')
    input_num = 2
    answer = 4
    print('ok' if answer == func(input_num) else 'fail')

    print('#2: ', end='')
    input_num = 7
    answer = 10
    print('ok' if answer == func(input_num) else 'fail')

    print('#3: ', end='')
    input_num = 60
    answer = 122
    print('ok' if answer == func(input_num) else 'fail')

    print('#4: ', end='')
    input_num = 750
    answer = 806
    print('ok' if answer == func(input_num) else 'fail', end='\n\n')


if __name__ == '__main__':
    # test(find_first_largest_value)

    print(find_first_largest_value(361527))
