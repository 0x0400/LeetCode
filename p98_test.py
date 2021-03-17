from p98 import Solution, TreeNode

test_cases = [
    ([2,1,3], True),
    ([5,1,4,None,None,3,6], False),
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

def test_isValidBST():
    s = Solution()
    for case in test_cases:
        assert s.isValidBST(buildTreeFromList(case[0])) == case[1], case
