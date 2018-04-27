'''http://adventofcode.com/2017/day/6'''


def reallocate_list(ls: list, val: int, index: int) -> list:
    '''
    Add 1 from val param to each element of list in cycle begin from index + 1 until out of val (val = 0).
    Return result list.
    '''
    while val > 0:
        if index == len(ls) - 1:
            index = 0
        else:
            index += 1
        ls[index] += 1
        val -= 1

    return ls


def count_cycles(ls: list) -> int:
    '''
    Finds highest element in list and redistributes these element among the list in cycles.
    Return how many redistribution cycles must be completed before function reallocate_list is produced not uniq list.
    '''
    uniq_ls = [tuple(ls)]
    while True:
        max_val = max(ls)
        max_index = ls.index(max_val)
        ls[max_index] = 0
        ls = reallocate_list(ls, max_val, max_index)
        if tuple(ls) not in uniq_ls:
            uniq_ls.append(tuple(ls))
        else:
            return len(uniq_ls)


def test(func):
    '''Test function'''
    print('Test: steps_count function.')

    print('#1: ', end='')
    input_list = [0, 2, 7, 0]
    answer = 5
    print('ok' if answer == func(input_list) else 'fail', end='\n\n')


if __name__ == '__main__':
    # test(count_cycles)

    with open('sources/memory_bank.txt', 'r') as file:
        for line in file:
            content = line.split()
            content = list(map(int, content))
    print(count_cycles(content))
