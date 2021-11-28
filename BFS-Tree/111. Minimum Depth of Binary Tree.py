from data_structure import BinaryTree, TreeNode


# Runtime: 480 ms, faster than 83.44% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 49.1 MB, less than 77.85% of Python3 online submissions for Minimum Depth of Binary Tree.

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        deepth = 0
        # base case
        if root is None:
            return deepth

        deepth = 1
        # init
        queue = [root]

        while len(queue) != 0:

            size = len(queue)
            # breath function - important to define the size to breath search
            for idx in range(size):

                node = queue[idx]

                left = node.left
                right = node.right

                if left is None and right is None:
                    return deepth

                if left is not None:
                    queue.append(left)

                if right is not None:
                    queue.append(right)

            deepth += 1
            queue = queue[size:]
            # pop out the size that have been searched


if __name__ == "__main__":
    null = None
    root = [2, null, 3, null, 4, null, 5, null, 6]
    binary_tree = BinaryTree()
    root = binary_tree(root)

    print(Solution().minDepth(root))
