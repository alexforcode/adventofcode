'''http://adventofcode.com/2017/day/5'''


def count_steps_to_exit(offsets: list):
    '''
    Return number of steps to reach the exit from list from file.
    Each element of list is offset for jumps through list.
    After each jump the offset of that jump decreases by 1, if the offset was three or more. Otherwise, increase by 1.
    '''
    jump, count_steps = 0, 0
    while jump < len(offsets):
        curr = jump
        jump += offsets[curr]
        if offsets[curr] >= 3:
            offsets[curr] -= 1
        else:
            offsets[curr] += 1
        count_steps += 1

    return count_steps


def test(func):
    '''Test function.'''
    print('#1: ', end='')
    answer = 10
    with open('sources/test.txt', 'r') as file:
        content = [int(line) for line in file]
        print('ok' if func(content) == answer else 'fail')


if __name__ == '__main__':
    # test(count_steps_to_exit)

    with open('sources/maze.txt', 'r') as file:
        content = [int(line) for line in file]
        print(count_steps_to_exit(content))
