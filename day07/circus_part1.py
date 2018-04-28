'''http://adventofcode.com/2017/day/7'''

import re


class Tower:
    def __init__(self, name, weight, branches):
        self.name = name
        self.weight = weight
        self.branches = branches


def find_tower(input_str: str) -> Tower:
    '''
    Return Tower object with name, weight and branches from  input_str.
    '''
    parts = input_str.split(' -> ')

    rgx = re.compile(r'(\w+)\s\((\d+)\)')
    match = rgx.match(parts[0])

    name, weight = match.groups()
    weight = int(weight)
    branches = parts[1].split(', ') if len(parts) > 1 else []

    return Tower(name, weight, branches)


def find_root(content: str) -> str:
    '''
    Return name of the bottom program in program tree from progs_str.
    '''
    towers = []
    parts = content.strip().split('\n')
    for part in parts:
        towers.append(find_tower(part.strip()))

    has_branches = set()
    are_branches = set()
    for tower in towers:
        if tower.branches:
            has_branches.add(tower)
        for branch in tower.branches:
            are_branches.add(branch)

    for tower in has_branches:
        if tower.name not in are_branches:
            return tower.name


def test(func):
    '''Test function'''
    print('Test: find_root function.')

    print('#1: ', end='')
    with open('sources/test.txt', 'r') as file:
        content = file.read()
    answer = 'tknk'
    print('ok' if answer == func(content) else 'fail', end='\n\n')


if __name__ == '__main__':
    # test(find_root)

    with open('sources/programs_tree.txt', 'r') as file:
        content = file.read()
    print(find_root(content))
