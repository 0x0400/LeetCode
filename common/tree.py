
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "<TreeNode:{}>".format(self.val)


def buildTreeFromList(vals):
    if not vals:
        return None
    head = TreeNode(vals[0])
    nodes = [head]
    for idx, val in enumerate(vals[1:]):
        if val is None:
            if idx%2 == 1:
                nodes.pop(0)
            continue
        curNode = TreeNode(val)
        nodes.append(curNode)
        if idx % 2 == 0:
            nodes[0].left = curNode
        else:
            nodes[0].right = curNode
            nodes.pop(0)
    return head

def getListFromTree(head: TreeNode):
    rst = []
    queue = [head]
    while queue and queue.count(None) != len(queue):
        node = queue.pop(0)
        if node is None:
            rst.append(None)
            queue.append(None)
            queue.append(None)
            continue

        rst.append(node.val)
        queue.append(node.left if node.left else None)
        queue.append(node.right if node.right else None)
    if rst and rst[-1] is None:
        rst.pop()
    return rst

def getListFromTreeV2(head: TreeNode):
    rst = []
    queue = [head]
    while queue and queue.count(None) != len(queue):
        node = queue.pop(0)
        if node is None:
            rst.append(None)
            continue

        rst.append(node.val)
        queue.append(node.left if node.left else None)
        queue.append(node.right if node.right else None)
    if rst and rst[-1] is None:
        rst.pop()
    return rst


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    # def __str__(self):
    #     return "Node<{}>".format(self.val)

def buildNAryTreeFromList(vals):
    if not vals:
        return None

    root = None
    queue = []
    curChildren = []
    for val in vals:
        if val is not None:
            node = Node(val)
            curChildren.append(node)
            queue.append(node)
            continue
        else:
            if not root:
                root = curChildren[0]
            else:
                parent = queue.pop(0)
                parent.children = curChildren
            curChildren = []
    if curChildren and queue:
        queue[0].children = curChildren
    return root
