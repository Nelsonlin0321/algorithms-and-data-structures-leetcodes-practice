from typing import List


class Solution:

    def partition(self, freqs: List[int], left: int, right: int):
        pivot = freqs[right]

        while left < right:
            while freqs[left] >= pivot and left < right:
                left += 1
            freqs[right] = freqs[left]

            while freqs[right] < pivot and left < right:
                right -= 1
            freqs[left] = freqs[right]

        freqs[left] = pivot

        return left, pivot

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  get the dictionary of frequency

        frequency_dict = {}
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1

        freqs = list(frequency_dict.values())

        top_k_value = None
        left = 0
        right = len(freqs)-1
        while True:
            index, pivot = self.partition(freqs, left, right)
            if index+1 == k:
                top_k_value = pivot
                break
            if index+1 > k:
                #  which means the target number on th left
                right = index - 1
            else:
                left = index + 1

        res = []
        for val, freq in frequency_dict.items():
            if freq >= top_k_value:
                res.append(val)

        return res
