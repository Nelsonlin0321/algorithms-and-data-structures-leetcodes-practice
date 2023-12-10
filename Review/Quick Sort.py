from typing import List


def partition(nums: List[int], left: int, right: int):
    pivot = nums[right]

    while left < right:

        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]

        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]

    nums[left] = pivot
    return left


def sort(nums: List[int], left: int, right: int):
    pivot = partition(nums=nums, left=left, right=right)

    if left < pivot-1:
        sort(nums=nums, left=left, right=pivot-1)

    if pivot+1 < right:
        sort(nums=nums, left=pivot+1, right=right)


if __name__ == "__main__":
    nums = [2, 4, 1, 3, 5, 3, 3]
    # pivot = partition(nums=nums, left=0, right=len(nums)-1)
    # print(nums)
    # print(pivot)
    sort(nums=nums, left=0, right=len(nums)-1)
    print(nums)
