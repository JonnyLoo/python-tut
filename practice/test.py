import mysum
import myreplace

import random

t1_cases = [
    [0, 0, 0, 0, 0],
    [1, 1, 1],
    [1, 2, 3, 0],
    [1, -2, 3, -4, 5, -6],
    [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
]

t2_cases = [
    ['abcdef', 'a', 'z'],
    ['abc', 'd', 'x'],
    ['aaaa', 'a', 'p']
]

class Test:
    def runall(self):
        self.t1()
        self.t2()

    def t1(self):
        print('\nTest mysum\n')
        for case in t1_cases:
            received = mysum.sum(case)
            expected = sum(case)
            if received == expected:
                print('PASSED')
            else:
                print('FAILED: Sum of {} should be {}, got {}'.format(case, expected, received))

    def t2(self):
        print('\nTest myreplace\n')
        for case in t2_cases:
            received = myreplace.replace(case[0], case[1], case[2])
            expected = case[0].replace(case[1], case[2])
            if received == expected:
                print('PASSED')
            else:
                print('FAILED: Word {} with {} replacing {} should be {}, got {}'.format(case[0], case[2], case[1], expected, received))

if __name__ == '__main__':
    print('RUNNING TESTS:')
    test = Test()
    test.runall()
    print('\nTESTS COMPLETE\n')
