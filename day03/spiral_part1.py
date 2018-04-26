'''http://adventofcode.com/2017/day/3'''


def ring_index(num):
    '''
    Return ring index of spiral and low / high numbers in that ring.
    '''
    n = 1
    ring = 0
    if num == 1:
        return ring
    while True:
        ring += 1
        low_num = n**2 + 1
        high_num = (n + 2)**2
        if num in range(low_num, high_num + 1):
            return ring, low_num, high_num
        n += 2


def steps_count(num):
    '''
    Return shortest path (smallest number of steps) from num to center (1) in spiral pattern.
    '''
    if num == 1:
        return 0
    ring, low_num, high_num = ring_index(num)
    elem_in_row = (high_num - low_num + 1) // 4
    while True:
        if num in range(high_num - elem_in_row, high_num):
            center_num = (high_num - elem_in_row + high_num) // 2
            steps_to_center = abs(num - center_num)
            break
        high_num -= elem_in_row
    return ring + steps_to_center


def test(func):
    '''Test function'''
    print('Test: steps_count function.')

    print('#1: ', end='')
    input_num = 1
    answer = 0
    print('ok' if answer == func(input_num) else 'fail')

    print('#2: ', end='')
    input_num = 12
    answer = 3
    print('ok' if answer == func(input_num) else 'fail')

    print('#3: ', end='')
    input_num = 23
    answer = 2
    print('ok' if answer == func(input_num) else 'fail')

    print('#4: ', end='')
    input_num = 1024
    answer = 31
    print('ok' if answer == func(input_num) else 'fail', end='\n\n')


if __name__ == '__main__':
    # test(steps_count)

    print(steps_count(361527))
