class Solution:

    def binary_search(self, arr, target) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = left + (right - left) // 2
            mid_num = arr[mid]
            if mid_num == target:
                return mid
            elif mid_num > target:
                right = mid - 1
            elif mid_num < target:
                left = mid + 1


arr = [1, 2, 3, 4, 5, 6, 7, 8]

print(Solution().binary_search(arr, 4))
