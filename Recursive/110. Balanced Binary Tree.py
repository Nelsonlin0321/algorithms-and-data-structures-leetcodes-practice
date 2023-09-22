# Definition for a binary tree node.
# Runtime: 56 ms, faster than 42.47% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 18 MB, less than 76.50% of Python3 online submissions for Balanced Binary Tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_height(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:

        # Conquer
        # Base Case
        if root is None:
            return True

        # Divide
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if abs(left_height - right_height) > 1:
            return False

        # Combine
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# Runtime: 44 ms, faster than 91.65% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 18 MB, less than 76.50% of Python3 online submissions for Balanced Binary Tree.
class Solution:
    def __init__(self):
        self.is_balanced = True

    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if abs(left_height - right_height) > 1:
            self.is_balanced = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: TreeNode) -> bool:

        # Conquer
        # Base Case
        if root is None:
            return True

        _ = self.get_height(root)

        return self.is_balanced


if __name__ == "__main__":
    print(True and True)
