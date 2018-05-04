''' http://adventofcode.com/2017/day/9 '''


def score(stream: str) -> int:
    '''
    Return total score for all groups in stream.
    '''
    total_score = 0
    depth = 0
    in_garbage = False
    negate = False

    for char in stream:
        if negate:
            negate = False
            continue
        elif char == '!':
            negate = True
        elif char == '<':
            in_garbage = True
        elif in_garbage:
            if char == '>':
                in_garbage = False
        elif char == '{':
            depth += 1
            total_score += depth
        elif char == '}':
            depth -= 1

    return total_score


def test(func):
    '''Test function'''
    print('Test: score function.')

    print('#1: ', end='')
    stream = '{}'
    answer = 1
    print('ok' if answer == func(stream) else 'fail')

    print('#2: ', end='')
    stream = '{{{}}}'
    answer = 6
    print('ok' if answer == func(stream) else 'fail')

    print('#3: ', end='')
    stream = '{{},{}}'
    answer = 5
    print('ok' if answer == func(stream) else 'fail')

    print('#4: ', end='')
    stream = '{{{},{},{{}}}}'
    answer = 16
    print('ok' if answer == func(stream) else 'fail')

    print('#5: ', end='')
    stream = '{<a>,<a>,<a>,<a>}'
    answer = 1
    print('ok' if answer == func(stream) else 'fail')

    print('#6: ', end='')
    stream = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
    answer = 9
    print('ok' if answer == func(stream) else 'fail')

    print('#7: ', end='')
    stream = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    answer = 9
    print('ok' if answer == func(stream) else 'fail')

    print('#8: ', end='')
    stream = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    answer = 3
    print('ok' if answer == func(stream) else 'fail')


if __name__ == '__main__':
    # test(score)

    with open('sources/stream.txt') as file:
        stream = file.read().strip()
    print(score(stream))
