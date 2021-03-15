from p92 import Solution, ListNode

test_cases = [
    (([1,2,3,4,5], 2, 4), [1,4,3,2,5]),
    (([5], 1, 1), [5]),
    (([1,2,3,4,5], 1, 5), [5,4,3,2,1]),
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


def test_reverseBetween():
    s = Solution()
    for case in test_cases:
        assert getValues(s.reverseBetween(getListNodes(case[0][0]), case[0][1], case[0][2])) == case[1], case
