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


def find_root(towers: list) -> str:
    '''
    Return name of the bottom program in program tree.
    '''
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


def find_unbalanced(towers: list):
    '''

    '''
    lookups = {tower.name: tower for tower in towers}

    def check(tower: Tower):
        '''

        '''
        subchecks = {name: check(lookups[name]) for name in tower.branches}
        subcheck_weights = {weight for weight, _ in subchecks.values()}
        is_balanced = len(subcheck_weights) <= 1
        weight = tower.weight + sum(weight for weight, _ in subchecks.values())

        if (len(subcheck_weights) > 1 and all(is_balanced for _, is_balanced in subchecks.values())):
            print('tower:', tower.name)
            for name, (total_weight, is_balanced) in subchecks.items():
                above_tower = lookups[name]
                print(name, total_weight, above_tower.weight)

        return weight, is_balanced

    root = lookups[find_root(towers)]
    check(root)


if __name__ == '__main__':
    with open('sources/programs_tree.txt', 'r') as file:
        towers = [find_tower(line.strip()) for line in file]
    find_unbalanced(towers)
