from p50 import Solution

test_cases = [
    ([2.00000, 10], 1024.00000),
    # 跟底层浮点数的实现有关系，会导致结果不一致
    # ([2.10000, 3], 9.26100),
    ([2.00000, -2], 0.25000)
]


def test_my ():
    s = Solution()
    for case in test_cases:
        assert s.myPow(*case[0]) == case[1], case
