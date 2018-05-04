''' http://adventofcode.com/2017/day/9 '''


def count_garbage(stream: str) -> int:
    '''
    Return non-canceled characters are within the garbage in stream.
    '''
    count = 0
    in_garbage = False
    negate = False

    for char in stream:
        if negate:
            negate = False
            continue
        elif char == '!':
            negate = True
        elif in_garbage:
            if char == '>':
                in_garbage = False
            else:
                count += 1
        elif char == '<':
            in_garbage = True

    return count


def test(func):
    '''Test function'''
    print('Test: count_garbage function.')

    print('#1: ', end='')
    stream = '<>'
    answer = 0
    print('ok' if answer == func(stream) else 'fail')

    print('#2: ', end='')
    stream = '<random characters>'
    answer = 17
    print('ok' if answer == func(stream) else 'fail')

    print('#3: ', end='')
    stream = '<<<<>'
    answer = 3
    print('ok' if answer == func(stream) else 'fail')

    print('#4: ', end='')
    stream = '<{!>}>'
    answer = 2
    print('ok' if answer == func(stream) else 'fail')

    print('#5: ', end='')
    stream = '<!!>'
    answer = 0
    print('ok' if answer == func(stream) else 'fail')

    print('#6: ', end='')
    stream = '<!!!>>'
    answer = 0
    print('ok' if answer == func(stream) else 'fail')

    print('#7: ', end='')
    stream = '<{o"i!a,<{i<a>'
    answer = 10
    print('ok' if answer == func(stream) else 'fail')


if __name__ == '__main__':
    # test(count_garbage)

    with open('sources/stream.txt') as file:
        stream = file.read().strip()
    print(count_garbage(stream))
