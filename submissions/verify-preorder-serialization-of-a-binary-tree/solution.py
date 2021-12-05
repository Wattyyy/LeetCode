from collections import deque


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = deque(preorder.split(","))
        if len(nodes) == 1:
            return nodes[0] == "#"
        queue = [nodes[0]]
        nodes.popleft()

        while 0 < len(nodes) and 0 < len(queue):
            new_queue = deque([])
            for _, nd in enumerate(queue):
                if nd == "#":
                    continue
                if len(nodes) < 2:
                    return False
                nd1 = nodes.popleft()
                nd2 = nodes.popleft()
                new_queue.append(nd1)
                new_queue.append(nd2)
            queue = new_queue

        return len(nodes) == 0
