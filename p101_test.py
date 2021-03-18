from p101 import Solution, TreeNode

test_cases = [
    ([1,2,2,3,4,4,3], True),
    ([1,2,2,None,3,None,3], False),
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

def test_isSymmetric():
    s = Solution()
    for case in test_cases:
        assert s.isSymmetric(buildTreeFromList(case[0])) == case[1], case
