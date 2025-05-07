class Solution(object):

    def mergeSort(self, arr):
        # base case
        # conquer
        if len(arr) <= 1:
            return arr

        # divide
        idx = len(arr) // 2
        left_arr = arr[:idx]
        right_arr = arr[idx:]

        # conquer / combine
        # importance: further to split by recursive mergeSort function
        return self.merge(self.mergeSort(left_arr), self.mergeSort(right_arr))

    def merge(self, left_arr, right_arr):
        res = []

        while left_arr and right_arr:
            if left_arr[0] <= right_arr[0]:
                res.append(left_arr.pop(0))
            else:
                res.append(right_arr.pop(0))

        res.extend(left_arr)
        res.extend(right_arr)

        return res


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 3, 2, 1, 4, 5, 7, 8, ]
    print(Solution().mergeSort(arr))
