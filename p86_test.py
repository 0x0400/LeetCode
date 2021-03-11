from p86 import Solution, ListNode

test_cases = [
    (([1,4,3,2,5,2], 3), [1,2,2,4,3,5]),
    (([2,1], 2), [1, 2]),
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


def test_partition():
    s = Solution()
    for case in test_cases:
        assert getValues(s.partition(getListNodes(case[0][0]), case[0][1])) == case[1], case
