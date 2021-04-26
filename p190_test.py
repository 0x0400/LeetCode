from p190 import Solution

test_cases = [
    (0b00000010100101000001111010011100, 964176192),
    (0b11111111111111111111111111111101, 3221225471),

]

def test_reverseBits():
    s = Solution()
    for case in test_cases:
        assert s.reverseBits(case[0]) == case[1], case

