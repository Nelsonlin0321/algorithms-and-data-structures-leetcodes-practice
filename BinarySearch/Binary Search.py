

from typing import List


def binary_search(nums: List[int], target: int):
    if not nums:
        return - 1

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left)//2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            # which means the target on the right of mid, so the mid need to be left
            left = mid+1

        if target < nums[mid]:
            right = mid-1

    return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 5]
    target = 4
    res = binary_search(nums=nums, target=target)
    print(res)
