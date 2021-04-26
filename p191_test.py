from p191 import Solution

test_cases = [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31),

]

def test_hammingWeight():
    s = Solution()
    for case in test_cases:
        assert s.hammingWeight(case[0]) == case[1], case

