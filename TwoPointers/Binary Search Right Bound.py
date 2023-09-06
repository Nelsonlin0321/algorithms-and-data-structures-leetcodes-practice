class Solution:

    def binary_search(self, arr, target) -> int:

        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = left + (right - left) // 2
            mid_num = arr[mid]

            if mid_num == target:
                if mid_num == len(arr)-1 or arr[mid + 1] != target:
                    return mid
                else:
                    left = mid + 1

            elif mid_num > target:
                right = mid - 1

            elif mid_num < target:
                left = mid + 1


arr = [1, 1, 2, 2, 2, 6, 7, 8]

print(Solution().binary_search(arr, 2))
