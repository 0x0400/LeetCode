from p28_1 import Solution as Solution1
from p28_2 import Solution as Solution2

test_cases = [
    ('hello', 'll', 2),
    ('aaaaa', 'bba', -1),
    ('a', 'a', 0),
    ('', '', 0),
]


def test_strStr1():
    s = Solution1()
    for case in test_cases:
        assert s.strStr(case[0], case[1]) == case[2]


def test_strStr2():
    s = Solution2()
    for case in test_cases:
        assert s.strStr(case[0], case[1]) == case[2]
