# https://leetcode.com/problems/merge-sorted-array/submissions/
# Runtime: 36 ms, faster than 67.04% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.4 MB, less than 30.89% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        m_idx = m - 1
        n_idx = n - 1
        curr_idx = len(nums1) - 1

        while (m_idx != -1 and n_idx != -1):
            if nums1[m_idx] > nums2[n_idx]:
                nums1[curr_idx] = nums1[m_idx]
                curr_idx -= 1
                m_idx -= 1
            elif nums1[m_idx] <= nums2[n_idx]:
                nums1[curr_idx] = nums2[n_idx]
                curr_idx -= 1
                n_idx -= 1

        if m_idx == -1 and n_idx != -1:  # 当 第一个数组已经排列到相应的位置，但是第二数组需要，逐个搬移到第一个数组上
            # for i in range(curr_idx + 1):
            #     nums1[i] = nums2[i]
            nums1[:curr_idx + 1] = nums2[:curr_idx + 1]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)

    print(nums1)
