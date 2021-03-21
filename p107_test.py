from p107 import Solution, TreeNode

test_cases = [
    ([3,9,20,None,None,15,7], [[15,7],[9,20],[3]]),
    ([1], [[1]]),
    ([], []),
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

def test_levelOrderBottom():
    s = Solution()
    for case in test_cases:
        assert s.levelOrderBottom(buildTreeFromList(case[0])) == case[1], case
