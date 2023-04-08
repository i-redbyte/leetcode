# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned = {}
        stack = [node]
        cloned[node] = Node(node.val)

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                cloned[curr].neighbors.append(cloned[neighbor])

        return cloned[node]
