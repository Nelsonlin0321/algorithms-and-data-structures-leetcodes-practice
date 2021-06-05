# https://leetcode.com/problems/binary-tree-right-side-view/
# Runtime: 24 ms, faster than 97.25% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 14.3 MB, less than 18.56% of Python3 online submissions for Binary Tree Right Side View.

class Solution:

    def __init__(self):
        self.res = []

    def rightSideView(self, root: TreeNode) -> List[int]:

        if root is None:
            return self.res

        queque = [root]

        while len(queque) != 0:

            size = len(queque)

            # only select the rightest one
            self.res.append(queque[-1].val)

            for idx in range(size):
                node = queque[idx]

                if node.left is not None:
                    queque.append(node.left)
                if node.right is not None:
                    queque.append(node.right)

            queque = queque[size:]
        return self.res
