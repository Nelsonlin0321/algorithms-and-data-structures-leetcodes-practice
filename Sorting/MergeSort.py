class Solution(object):

    def mergeSort(self, arr):
        # base case
        # conqure
        if len(arr) <= 1:
            return arr

        # divide
        idx = len(arr) // 2
        left_arr = arr[:idx]
        right_arr = arr[idx:]

        # conqure / combine
        return self.merge(self.mergeSort(left_arr), self.mergeSort(right_arr))

    def merge(self, left_arr, right_arr):
        res = []

        while left_arr and right_arr:
            if left_arr[0] <= right_arr[0]:
                res.append(left_arr.pop(0))
            else:
                res.append(right_arr.pop(0))

        while left_arr:
            res.append(left_arr.pop(0))

        while right_arr:
            res.append(right_arr.pop(0))
        return res


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 3, 2, 1, 4, 5, 7, 8, ]
    print(Solution().mergeSort(arr))
