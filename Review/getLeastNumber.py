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


# nums = [3, 5, 6, 7, 3, 2, 4, 6, 9, 10, 16, 8]
# partition(nums, 0, len(nums) - 1)
# print(nums)


def recursive_find(nums, left, right, k):
    if left < right:
        pivot_index = partition(nums, left, right)
        if pivot_index + 1 == k:
            return nums[pivot_index]

        if pivot_index + 1 > k:
            return recursive_find(nums, left, pivot_index - 1, k)

        if pivot_index + 1 < k:
            return recursive_find(nums, pivot_index + 1, right, k)
    return nums[left]


nums = [-1, 2, 3, 5, 6, 7, 3, 2, 4, 6, 9, 10, 16, 8]

least_number = recursive_find(nums, 0, len(nums) - 1, 2)
print(least_number)
print(nums)
