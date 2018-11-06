from p31 import Solution as Solution

test_cases = [
    ([1, 2, 3], [1, 3, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 5], [1, 5, 1]),
    ([1, 3, 2], [2, 1, 3]),
    ([2, 3, 1], [3, 1, 2]),
    ([5,4,7,5,3,2], [5,5,2,3,4,7]),
]


def test_nextPermutation():
    s = Solution()
    for case in test_cases:
        print(case)
        s.nextPermutation(case[0])
        assert case[0] == case[1]
