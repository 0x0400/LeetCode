from p216 import Solution

test_cases = [
    [[3, 7], [[1,2,4]]],
    [[3, 9], [[1,2,6],[1,3,5],[2,3,4]]],
    [[4, 1], []],
    [[3, 2], []],
    [[9, 45], [[1,2,3,4,5,6,7,8,9]]],
]

def test_combinationSum3():
    s = Solution()
    for case in test_cases:
        assert sorted(s.combinationSum3(*case[0])) == sorted(case[1]), case

