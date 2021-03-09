from p82 import Solution, ListNode

test_cases = [
    ([1,2,3,3,4,4,5], [1,2,5]),
    ([1,1,1,2,3], [2, 3]),
    ([], []),
    ([1,1], []),
]

def getListNodes(nums):
    lastNode = None
    for val in reversed(nums):
        node = ListNode(val, lastNode)
        lastNode = node
    return lastNode

def getValues(head: ListNode):
    rst = []
    curNode = head
    while curNode:
        rst.append(curNode.val)
        curNode = curNode.next
    return rst


def test_deleteDuplicates():
    s = Solution()
    for case in test_cases:
        assert getValues(s.deleteDuplicates(getListNodes(case[0]))) == case[1], case
