from typing import List


class Solution:
    """
    Runtime: 60 ms, faster than 83.70% of Python3 online submissions for Two Sum II - Input array is sorted.
    Memory Usage: 14.7 MB, less than 33.72% of Python3 online submissions for Two Sum II - Input array is sorted.
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
