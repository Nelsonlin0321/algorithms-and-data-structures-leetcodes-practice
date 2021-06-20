from data_structure import TreeNode, array_binary_tree


# unsloved
class Solution:
    def rob(self, root: TreeNode) -> int:

        nums = self.BFS(root)

        # base case
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for t in range(2, len(nums)):
            dp[t] = max(dp[t - 2] + nums[t], dp[t - 1])

        return dp[-1]

    def BFS(self, root):
        layer_sum = []

        if root is None:
            return layer_sum

        queque = [root]

        while len(queque) != 0:

            agg_sum = 0

            size = len(queque)

            for idx in range(size):

                # node = queque.pop(idx)
                node = queque[idx]
                agg_sum += node.val

                # breath function
                if node.left is not None:
                    queque.append(node.left)

                if node.right is not None:
                    queque.append(node.right)

            layer_sum.append(agg_sum)

            queque = queque[size:]

        return layer_sum


class Solution:
    """
    Runtime: 48 ms, faster than 79.35% of Python3 online submissions for House Robber III.
    Memory Usage: 16.8 MB, less than 29.24% of Python3 online submissions for House Robber III.
    """

    def __init__(self):
        self.dp_dict = {}

    def rob(self, root: TreeNode) -> int:
        # the smallest problem
        if root is None:
            return 0

        if root in self.dp_dict:
            return self.dp_dict[root]

        # do it 抢 再抢下下家

        left_val = 0

        if root.left is not None:
            left_val = self.rob(root.left.left) + self.rob(root.left.right)

        right_val = 0
        if root.right is not None:
            right_val = self.rob(root.right.left) + self.rob(root.right.right)

        do_it = root.val + left_val + right_val

        # not do 不抢 抢下家

        not_do_it = self.rob(root.left) + self.rob(root.right)

        self.dp_dict[root] = max(not_do_it, do_it)

        return self.dp_dict[root]


if __name__ == "__main__":
    null = None
    root = [3, 2, 3, null, 3, null, 1]
    root = array_binary_tree(root)

    print(Solution().rob(root))
