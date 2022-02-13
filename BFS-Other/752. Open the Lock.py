"""https://leetcode.com/problems/open-the-lock/"""
from typing import List

"""Runtime: 812 ms, faster than 61.59% of Python3 online submissions for Open the Lock.
Memory Usage: 15.7 MB, less than 26.43% of Python3 online submissions for Open the Lock."""


class Solution:

    def __init__(self):
        self.visited_dict = {}

    def turnUp(self, passcode, pos):
        passcode = list(passcode)
        if passcode[pos] == '9':
            passcode[pos] = '0'
        else:
            passcode[pos] = str(int(passcode[pos]) + 1)
        return "".join(passcode)

    def turnDown(self, passcode, pos):
        passcode = list(passcode)
        if passcode[pos] == '0':
            passcode[pos] = '9'
        else:
            passcode[pos] = str(int(passcode[pos]) - 1)
        return "".join(passcode)

    # 广度传播函数
    def get_breath(self, passcode, deadends):

        passcodes = []
        for i in range(4):
            new_passcode = self.turnUp(passcode, i)
            if new_passcode not in deadends and new_passcode not in self.visited_dict:
                passcodes.append(new_passcode)
            new_passcode = self.turnDown(passcode, i)
            if new_passcode not in deadends and new_passcode not in self.visited_dict:
                passcodes.append(new_passcode)
        return passcodes

    def BFS(self, deadends, target):

        deadends = set(deadends)  # improve indexing

        queue = ["0000"]
        step = 0
        while len(queue) != 0:
            size = len(queue)

            for index in range(size):

                curr_passcode = queue[index]

                if curr_passcode in deadends or curr_passcode in self.visited_dict:
                    continue

                if curr_passcode == target:
                    return step

                # breath_function
                passcodes = self.get_breath(curr_passcode, deadends)

                if target in passcodes:
                    return step + 1

                self.visited_dict[curr_passcode] = True

                queue.extend(passcodes)

            step += 1
            queue = queue[size:]

        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        return self.BFS(deadends, target)


"""
Runtime: 456 ms, faster than 95.08% of Python3 online submissions for Open the Lock.
Memory Usage: 15.1 MB, less than 93.82% of Python3 online submissions for Open the Lock.
"""


class Solution:

    def __init__(self):
        self.visited_dict = {}

    def turnUp(self, passcode, pos):
        passcode = list(passcode)
        if passcode[pos] == '9':
            passcode[pos] = '0'
        else:
            passcode[pos] = str(int(passcode[pos]) + 1)
        return "".join(passcode)

    def turnDown(self, passcode, pos):
        passcode = list(passcode)
        if passcode[pos] == '0':
            passcode[pos] = '9'
        else:
            passcode[pos] = str(int(passcode[pos]) - 1)
        return "".join(passcode)

    def get_breath(self, passcode, deadends):

        passcodes = []
        for i in range(4):
            new_passcode = self.turnUp(passcode, i)
            if new_passcode not in deadends and new_passcode not in self.visited_dict:
                passcodes.append(new_passcode)
            new_passcode = self.turnDown(passcode, i)
            if new_passcode not in deadends and new_passcode not in self.visited_dict:
                passcodes.append(new_passcode)
        return passcodes

    def BiBFS(self, deadends, target):

        deadends = set(deadends)
        queue_1 = ["0000"]
        queue_2 = [target]

        step = 0
        while len(queue_1) != 0 and len(queue_2) != 0:

            size_1 = len(queue_1)
            temp = []
            for index in range(size_1):

                curr_passcode = queue_1[index]

                if curr_passcode in deadends or curr_passcode in self.visited_dict:
                    continue

                if curr_passcode in queue_2:
                    return step

                # breath_function
                passcodes = self.get_breath(curr_passcode, deadends)
                temp.extend(passcodes)
                self.visited_dict[curr_passcode] = True

            step += 1
            queue_1 = queue_2
            queue_2 = temp

        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        return self.BiBFS(deadends, target)


if __name__ == "__main__":
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    print(Solution().openLock(deadends, target))
