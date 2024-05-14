var_list = [2, 3, 4, 5, 321, 1]


class Solution(object):
    def bubble_sort(self, numbers):
        """
        :type numbers: List[int]
        """

        for i in range(
                len(numbers) - 1,  # start index
                -1, # 0 is not included
                -1
        ):
            for j in range(i): # important: if the start idx = 5, so j will be 4
                num_1 = numbers[j + 1]
                num_2 = numbers[j]
                if num_1 < num_2:
                    numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]


solution = Solution()
solution.bubble_sort(var_list)
print(var_list)
