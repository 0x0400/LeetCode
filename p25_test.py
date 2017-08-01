from p25 import Solution, ListNode


def test_reverseKGroup():
    s = Solution()

    sentinel = current = ListNode(0)
    for x in range(1, 6):
        current.next = ListNode(x)
        current = current.next
    result = s.reverseKGroup(sentinel.next, 2)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [2, 1, 4, 3, 5]

    sentinel = current = ListNode(0)
    for x in range(1, 6):
        current.next = ListNode(x)
        current = current.next
    result = s.reverseKGroup(sentinel.next, 3)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [3, 2, 1, 4, 5]
