from typing import List

"""
https://leetcode.com/problems/all-paths-from-source-to-target/submissions/1645049614/
Runtime
3ms
Beats93.58%
Analyze Complexity
Memory
18.96MB
Beats84.35%

"""


class Solution:

    def __init__(self):
        self.paths = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.backtracking(0, graph, [0])
        return self.paths

    def backtracking(self, src, graph, on_path):
        target = len(graph)-1

        if src == target:
            self.paths.append(on_path.copy())
            return

        nodes = graph[src]

        for node in nodes:
            on_path.append(node)
            self.backtracking(node, graph, on_path)
            on_path.pop()
