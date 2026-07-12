from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                # Connect to the next node in the same level
                if i < size - 1:
                    node.next = q[0]

                # Add children for the next level
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root