from p179 import Solution

test_cases = [
    ([10,2], "210"),
    ([3,30,34,5,9], "9534330"),
    ([1], "1"),
    ([10], "10"),
    ([432,43243], "43243432"),
    ([0, 0], "0"),
]

def test_largestNumber():
    for case in test_cases:
        s = Solution()
        assert s.largestNumber(case[0]) == case[1], case

def test_largestNumberV2():
    for case in test_cases:
        s = Solution()
        assert s.largestNumberV2(case[0]) == case[1], case
