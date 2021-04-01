# https://leetcode.com/problems/clone-graph/


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        root = Node(node.val)
        nodeCache = {node.val: root}
        nodeTodo = {node.val: node}
        nodeDone = {}

        while nodeTodo:
            for val, srcNode in list(nodeTodo.items()):
                if val not in nodeCache:
                    nodeCache[val] = Node(val)
                curNode = nodeCache[val]

                for neighbor in srcNode.neighbors:
                    if neighbor.val not in nodeCache:
                        nodeCache[neighbor.val] = Node(neighbor.val)
                    curNode.neighbors.append(nodeCache[neighbor.val])
                    if neighbor.val not in nodeDone:
                        nodeTodo[neighbor.val] = neighbor
                nodeTodo.pop(curNode.val)
                nodeDone[curNode.val] = curNode
        return root
