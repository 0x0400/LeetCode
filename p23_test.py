from p23 import Solution, ListNode


def test_mergeKLists():
    s = Solution()
    assert s.mergeKLists([]) == None

    lists = []
    for vals in [[1, 3, 5], [2, 4, 6], [7, 8, 9], [0, 10, 11]]:
        sentinel = current = ListNode(0)
        for val in vals:
            current.next = ListNode(val)
            current = current.next
        lists.append(sentinel.next)
    result = s.mergeKLists(lists)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == list(range(0, 12))
