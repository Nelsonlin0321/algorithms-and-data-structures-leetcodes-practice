from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # base case
        if root is None:
            return 0

        queue = Queue()
        queue.put(root)
        depth = 1

        while not queue.empty():
            size = queue.qsize()

            for _ in range(size):
                node = queue.get()

                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.put(node.left)

                if node.right:
                    queue.put(node.right)

            depth += 1

        return depth


if __name__ == "__main__":
    from data_structure import convert_array_binary_tree
    null = None
    root = [3, 9, 20, null, null, 15, 7]
    root = convert_array_binary_tree(root)
    res = Solution().minDepth(root)
    print(res)
