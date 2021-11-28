from typing import List


class Solution:
    def MergeSort(self, nums: List[int]) -> List[int]:
        # base case
        if len(nums) <= 1:
            return nums

        idx = len(nums) // 2

        left_nums = nums[:idx]
        right_nums = nums[idx:]

        # important:  left_nums and right_nums need to be further split
        return self.Merge(
            self.MergeSort(left_nums),
            self.MergeSort(right_nums)
        )

    def Merge(self, nums_1, nums_2):
        # nums_1 is sorted
        # nums_2 is sorted

        # from the smallest and largest
        merge_res = []
        while nums_1 and nums_2:  # not empty

            if nums_1[0] <= nums_2[0]:
                merge_res.append(nums_1.pop(0))
            else:
                merge_res.append(nums_2.pop(0))

        while nums_1:
            merge_res.extend(nums_1)
            nums_1 = []

        while nums_2:
            merge_res.extend(nums_2)
            nums_2 = []

        return merge_res


if __name__ == "__main__":
    numbers = [4, 5, 6, 78, 3, 2,0, 4, 6]
    print(Solution().MergeSort(numbers))
