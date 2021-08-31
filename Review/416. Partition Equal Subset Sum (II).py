from typing import List


class Solution:
    """
    Runtime: 3672 ms, faster than 14.24% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 29.7 MB, less than 43.80% of Python3 online submissions for Partition Equal Subset Sum.
    """

    def canPartition(self, nums: List[int]) -> bool:
        # base case
        if len(nums)<=1:
            return False

        list_sum  = sum(nums)

        if list_sum % 2 !=0:
            return False

        target_sum = list_sum//2

        # design dp table
        M = [None for _ in range(target_sum+1)]
        dp = [M.copy() for _ in range(len(nums)+1)]
        # dp[N][M] # N item, M is the sum

        #sub-problem definition: for a certain size of package, and the top N item , is there any way to fill extractly.

        #base case
        # no item -> unfilled
        for idx in range(target_sum+1):
            dp[0][idx] = False

        # no more package size, which means filled
        for idx in range(len(nums)+1):
            dp[idx][0] = True


        for m in range(1,len(M)):
            for n in range(1,len(nums)+1):
                weight = nums[n-1]
                if weight>m: # cannot install
                    dp[n][m] = dp[n-1][m]
                else:
                    # fill or not fill
                    dp[n][m] = dp[n-1][m] or dp[n-1][m-weight]

        return dp[-1][-1]

if __name__ == "__main__":
    nums = [1,2,3,5]
    print(Solution().canPartition(nums))






