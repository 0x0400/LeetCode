from p106 import Solution, TreeNode

test_cases = [
    (([9,3,15,20,7], [9,15,7,20,3]), [3,9,20,None,None,15,7]),
    (([-1], [-1]), [-1]),
    (([2, 1], [2, 1]), [1, 2]),
    (([2, 3, 1], [3, 2, 1]), [1, 2, None, None, 3])
]

def getListFromTree(head: TreeNode):
    rst = []
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node is None:
            rst.append(None)
            continue
        rst.append(node.val)
        queue.append(node.left if node.left else None)
        queue.append(node.right if node.right else None)
    while rst and rst[-1] == None:
        rst.pop()
    return rst

def test_buildTree():
    s = Solution()
    for case in test_cases:
        assert getListFromTree(s.buildTree(*case[0])) == case[1], case
