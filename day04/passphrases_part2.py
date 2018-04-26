'''http://adventofcode.com/2017/day/4'''


def check_passphrases(file):
    '''
    Return the number of valid passphrases (phrase contain no two words that are anagrams of each other) from file.
    '''
    content = [line.strip() for line in file]

    valid_count = 0
    for line in content:
        words = line.split()
        non_anagrams = {tuple(sorted(word)) for word in words}  # set of words
        if len(words) == len(non_anagrams):
            valid_count += 1

    return valid_count


def test(func):
    '''Test function/'''
    print('#1: ', end='')
    answer = 3
    with open('sources/test_part2.txt', 'r') as file:
        print('ok' if func(file) == answer else 'fail')


if __name__ == '__main__':
    # test(check_passphrases)

    with open('sources/passphrases.txt', 'r') as file:
        print(check_passphrases(file))
