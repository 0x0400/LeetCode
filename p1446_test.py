from p1446 import Solution

test_cases = [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
    ("triplepillooooow", 5),
    ("hooraaaaaaaaaaay", 11),
    ("tourist", 1),
    ("j", 1),
]

def test_maxPower():
    s = Solution()
    for case in test_cases:
        assert s.maxPower(case[0]) == case[1], case
