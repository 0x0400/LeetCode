from p24 import Solution, ListNode


def test_swapPairs():
    s = Solution()

    assert s.swapPairs(None) is None

    sentinel = current = ListNode(0)
    for x in [1, 2, 3, 4]:
        current.next = ListNode(x)
        current = current.next
    result = s.swapPairs(sentinel.next)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [2, 1, 4, 3]
