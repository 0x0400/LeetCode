from p100 import Solution, TreeNode

test_cases = [
    (([1,2,3], [1,2,3]), True),
    (([1,2], [1,None,2]), False),
    (([1,2,1], [1,1,2]), False),
]

def buildTreeFromList(vals):
    if not vals:
        return None
    head = TreeNode(vals[0])
    nodes = [head]
    for idx, val in enumerate(vals[1:]):
        if val is None:
            continue
        curNode = TreeNode(val)
        nodes.append(curNode)
        if idx % 2 == 0:
            nodes[0].left = curNode
        else:
            nodes[0].right = curNode
            nodes.pop(0)
    return head

def test_isSameTree():
    s = Solution()
    for case in test_cases:
        assert s.isSameTree(buildTreeFromList(case[0][0]), buildTreeFromList(case[0][1])) == case[1], case
