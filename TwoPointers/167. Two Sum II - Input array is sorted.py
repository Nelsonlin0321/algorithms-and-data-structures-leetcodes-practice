# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Runtime: 44 ms, faster than 82.36% of Python online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 13.6 MB, less than 68.31% of Python online submissions for Two Sum II - Input array is sorted.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # arr is sorted
        low_idx = 0
        hig_idx = len(arr) - 1

        while low_idx < hig_idx:
            sum = arr[low_idx] + arr[hig_idx]
            if sum == target:
                return [low_idx + 1, hig_idx + 1]
            elif sum > target:
                hig_idx -= 1
            elif sum < target:
                low_idx += 1
        return -1


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    sum_up = solution.twoSum(arr, target)
    print(sum_up)
