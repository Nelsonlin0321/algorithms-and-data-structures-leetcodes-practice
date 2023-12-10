from typing import List


def sort(nums: List[int], left: int, right: int):

    if left < right:
        p = left + (right - left)//2
        nums1 = sort(nums=nums, left=left, right=p)
        nums2 = sort(nums=nums, left=p+1, right=right)
        return merge(nums1, nums2)

    return nums[left:right+1]


def merge(nums1: List[int], nums2: List[int]):

    left = 0
    right = 0
    mergeList = []

    while 0 <= left < len(nums1) and 0 <= right < len(nums2):
        if nums1[left] <= nums2[right]:
            mergeList.append(nums1[left])
            left += 1
        else:
            mergeList.append(nums2[right])
            right += 1

    while 0 <= left < len(nums1):
        mergeList.append(nums1[left])
        left += 1

    while 0 <= right < len(nums2):
        mergeList.append(nums2[right])
        right += 1

    return mergeList


if __name__ == "__main__":
    # nums1 = [1, 2, 3, 5, 6]
    # nums2 = [2, 2, 8, 10, 11]
    # mergeList = merge(nums1, nums2)
    # print(mergeList)

    nums = [12, 4, 12, 3, 4, 5, 6, 3, 2]
    res = sort(nums=nums, left=0, right=len(nums)-1)
    print(res)
