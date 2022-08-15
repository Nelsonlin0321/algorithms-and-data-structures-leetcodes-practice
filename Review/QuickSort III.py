# [!important: to inplace put the number left, smaller or equal to pivot, and right, larger than pivot ]

# ascending
def partition(nums, left, right):
    pivot = nums[right]
    # after this, right index position is taken for replacement

    while left < right:
        # From the smallest to the largest
        # [!important]: Move left index until the right
        while nums[left] <= pivot and left < right:
            left += 1
        nums[right] = nums[left]
        # after this, left index position is taken for replacement

        while nums[right] > pivot and left < right:
            right -= 1
        nums[left] = nums[right]

    nums[left] = pivot

    return left

# descending
def partition(nums, left, right):
    pivot = nums[left]
    # after this, right index position is taken for replacement

    while left < right:
        # From the largest to the smallest
        # [!important]: Move left index until the right
        while nums[right] <= pivot and left < right:
            right -= 1
        nums[left] = nums[right]
        # after this, left index position is taken for replacement

        while nums[left] > pivot and left < right:
            left += 1
        nums[right] = nums[left]

    nums[left] = pivot

    return left


# [!important] : Recursive logic to partition
def recursive_partition(nums, left, right):
    if left < right:
        pivot_idx = partition(nums, left, right)
        recursive_partition(nums, left, pivot_idx - 1)
        recursive_partition(nums, pivot_idx + 1, right)


def quickSort(nums):
    # if len(nums) <= 1:
    #     return nums

    left = 0
    right = len(nums) - 1
    recursive_partition(nums, left, right)


nums = [4, 7, 8, 4, 3, 6, 7, 8, 9, 4, 2, 1]
quickSort(nums)
print(nums)
