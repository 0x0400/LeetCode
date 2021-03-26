from p118 import Solution

test_cases = [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]]),
]

def test_generate():
    s = Solution()
    for case in test_cases:
        assert s.generate(case[0]) == case[1], case
