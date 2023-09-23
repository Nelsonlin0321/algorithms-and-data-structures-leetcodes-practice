from queue import Queue
from typing import Optional
import sys
sys.path.insert(0, "./../")
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = Queue()
        q.put(root)
        # root 本身就是一层，depth 初始化为 1
        depth = 1

        while not q.empty():

            sz = q.qsize()
            # 将当前队列中的所有节点向四周扩散
            for i in range(sz):
                cur = q.get()
                # 判断是否到达终点
                if not cur.left and not cur.right:
                    return depth
                # 将 cur 的相邻节点加入队列
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            # 这里增加步数
            depth += 1

        return depth


if __name__ == "__main__":
    from data_structure import convert_array_binary_tree
    null = None
    root = [3, 9, 20, null, null, 15, 7]
    root = convert_array_binary_tree(root)
    res = Solution().minDepth(root)
    print(res)
