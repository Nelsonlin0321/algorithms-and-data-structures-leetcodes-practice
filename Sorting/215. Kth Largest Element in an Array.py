from typing import List
"""
TimeOut
"""

def partition(nums, left, right):
    pivot = nums[right]

    while left < right:
        while nums[left] <= pivot and left < right:
            left += 1
        nums[right] = nums[left]

        while nums[right] > pivot and left < right:
            right -= 1
        nums[left] = nums[right]

    nums[left] = pivot

    return left


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        left = 0
        right = len(nums)-1

        while True:
            pivot_idx = partition(nums, left, right)
            th_largest = len(nums)-pivot_idx
            pivot_num = nums[pivot_idx]
            if th_largest == k:
                return pivot_num
            if th_largest > k:
                # the target value [k] is larger, on the right, to shrink the left
                left = pivot_idx+1
            else:
                right = pivot_idx-1


"""
Runtime
Details
509ms
Beats 42.82%of users with Python3
Memory
Details
29.68MB
Beats 34.88%of users with Python3
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_value = min(nums)
        max_value = max(nums)

        bucket_list = [[] for _ in range(min_value,max_value+1)]
        
        for num in nums:
            bucket_list[num-min_value].append(num)


        sort_list = []

        for bucket in bucket_list[::-1]:
            if len(sort_list)<k:
                sort_list.extend(bucket)
            else:
                break
        
        return sort_list[k-1]

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    res = Solution().findKthLargest(nums, k)
    print(res)