from typing import List


def can_be_formed_by_deleting(s: str, d: str):

    i = 0
    j = 0

    while i < len(s) and j < len(d):
        s_char = s[i]
        d_char = d[j]

        if s_char == d_char:
            i += 1
            j += 1
        else:
            i += 1

    return j == len(d)


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary)
        dictionary = sorted(dictionary, key=len, reverse=True)

        for d in dictionary:
            if can_be_formed_by_deleting(s, d):
                return d

        return []


if __name__ == "__main__":
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    res = Solution().findLongestWord(s, dictionary)
    print(res)
