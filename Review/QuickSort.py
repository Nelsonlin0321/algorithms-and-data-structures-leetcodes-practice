class Solution:

    def quickSort(self, array):

        self.recursive_partition(array, 0, len(array) - 1)

    def recursive_partition(self, array, left, right):

        # conquer
        if left >= right:
            return
            # no need to sort

        # divide
        pivot = self.partition(array, left, right)
        self.recursive_partition(array, left, pivot - 1)
        self.recursive_partition(array, pivot + 1, right)

        # no need to combine because it's inplace partition

    def partition(self, array, left, right):
        # 最右边已经取出了
        pivot = array[right]

        while left < right:

            while left < right and array[left] <= pivot:
                left += 1

            # 当 left 不再 <=pivot 了， 得移动到右边去
            array[right] = array[left]

            while left < right and array[right] > pivot:
                right -= 1

            # 当 right 不再 > pivot 了， 得移动到左边去
            array[left] = array[right]

        # left 与 right 相遇，该位置就是pivot
        array[right] = pivot

        return right

    # no need to combine


if __name__ == "__main__":
    array = [5, 2, 6, 7, 3, 1, 4, 7, 4, 10]
    # pivot = partition(array, 0, len(array) - 1)
    # print(pivot)
    # print(array)
    Solution().quickSort(array)
    print(array)
