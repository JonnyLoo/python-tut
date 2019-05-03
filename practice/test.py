import q1

t1_cases = [
    [0, 0, 0],
    [1, 1, 1]
]

class Test:
    def runall(self):
        self.t1()

    def t1(self):
        for case in t1_cases:
            if q1.sum(case) == sum(case):
                print('PASSED')
            else:
                print('FAILED: Sum should be {}, got {}'.format(sum(case), q1.sum(case)))


if __name__ == '__main__':
    print('RUNNING TESTS:\n')
    test = Test()
    test.runall()
    print('\nTESTS COMPLETE\n')
