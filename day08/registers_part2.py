'''http://adventofcode.com/2017/day/8'''


def find_max_register(insts: list) -> int:
    '''
    Return higest value in any register during completing the instructions from inst list
    '''
    ops = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '>=': lambda x, y: x >= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
        'inc': lambda x, y: x + y,
        'dec': lambda x, y: x - y
    }

    regs = {}
    for line in insts:
        if line[0] not in regs:
            regs[line[0]] = 0

    max_val = 0
    for inst in insts:
        if ops[inst[5]](regs[inst[4]], int(inst[6])):
            regs[inst[0]] = ops[inst[1]](regs[inst[0]], int(inst[2]))
        if max(regs.values()) > max_val:
            max_val = max(regs.values())

    return max_val


def test(func):
    '''Test function'''
    print('Test: find_max_register function.')

    print('#1: ', end='')
    with open('sources/test.txt', 'r') as file:
        insts = [line.split() for line in file]
    answer = 10
    print('ok' if answer == func(insts) else 'fail', end='\n\n')


if __name__ == '__main__':
    # test(find_max_register)

    with open('sources/instructions.txt') as file:
        insts = [line.split() for line in file]

    print(find_max_register(insts))
