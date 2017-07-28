from p19 import Solution


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def test_letterCombinations():
    s = Solution()
    head = current = ListNode(0)
    for x in [1, 2, 3, 4, 5]:
        current.next = ListNode(x)
        current = current.next
    result = s.removeNthFromEnd(head.next, 2)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [1, 2, 3, 5]
