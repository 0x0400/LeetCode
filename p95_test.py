from typing import List
from p95 import Solution, TreeNode

test_cases = [
    (3, [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]]),
    (1, [[1]]),
]


# def getListFromTree(head: TreeNode):
#     rst = []
#     queue = [(0, head)]
#     while queue:
#         idx, node = queue.pop(0)
#         if idx >= len(rst):
#             rst += [None] * (idx+1-len(rst))
#         rst[idx] = node.val
#         if node.left:
#             queue.append((idx*2+1, node.left))
#         if node.right:
#             queue.append((idx*2+2, node.right))
#     return rst

def getListFromTree(head: TreeNode):
    rst = []
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node is None:
            rst.append(None)
            continue
        rst.append(node.val)
        if node.left or node.right:
            queue.append(node.left if node.left else None)
            queue.append(node.right if node.right else None)
    if rst and rst[-1] == None:
        rst.pop()
    return rst


def test_generateTrees():
    s = Solution()
    for case in test_cases:
        assert [getListFromTree(plan) for plan in s.generateTrees(case[0])] == case[1], case
