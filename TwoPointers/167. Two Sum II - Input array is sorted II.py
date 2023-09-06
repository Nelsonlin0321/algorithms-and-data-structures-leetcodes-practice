
"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

"""
from typing import List

"""
Runtime: 60 ms, faster than 88.65% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.6 MB, less than 63.21% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init the left and right pointer
        left = 0
        right = len(numbers)-1

        while (left < right):
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left+1,right +1]
            elif sum_< target:
                left +=1
            elif sum_ > target:
                right -=1


