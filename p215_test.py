from p215 import Solution

test_cases = [
    [[[3,2,1,5,6,4], 2], 5],
    [[[3,2,3,1,2,4,5,5,6], 4], 4],
]

def test_findKthLargest():
    s = Solution()
    for case in test_cases:
        assert s.findKthLargest(*case[0]) == case[1], case

def test_findKthLargestQS():
    s = Solution()
    for case in test_cases:
        assert s.findKthLargestQS(*case[0]) == case[1], case
