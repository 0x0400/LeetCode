from p21 import Solution, ListNode


def test_mergeTwoLists():
    s = Solution()
    l1 = current = ListNode(0)
    for x in [1, 3, 5]:
        current.next = ListNode(x)
        current = current.next
    l2 = current = ListNode(0)
    for x in [2, 4, 6]:
        current.next = ListNode(x)
        current = current.next
    result = s.mergeTwoLists(l1.next, l2.next)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [1, 2, 3, 4, 5, 6]
