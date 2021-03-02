from p61 import Solution, ListNode

test_cases = [
    (([1,2,3,4,5], 2), [4,5,1,2,3]),
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


def test_rotateRight():
    s = Solution()
    for case in test_cases:
        assert getValues(s.rotateRight(getListNodes(case[0][0]), case[0][1])) == case[1], case

