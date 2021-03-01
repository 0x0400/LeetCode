from p57_v2 import Solution

test_cases = [
    # (([[1,3],[6,9]], [2,5]), [[1,5],[6,9]]),
    # (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]]),
    # (([],[5,7]), [[5,7]]),
    (([[1,5],[6,8]], [0, 9]), [[0, 9]])
]


def test_insert():
    s = Solution()
    for case in test_cases:
        assert s.insert(*case[0]) == case[1], case
