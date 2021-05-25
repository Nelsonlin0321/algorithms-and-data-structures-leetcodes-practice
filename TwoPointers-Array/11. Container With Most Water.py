# Time Limit Exceeded
class Solution:
    def helper(self,height, left, right):
        width = right - left
        height = min(height[left], height[right])
        area = width * height

        return area

    def maxArea(self,height):
        max_area = 0
        for idx in range(len(height) - 1):
            for jdx in range(idx + 1, len(height)):
                area = self.helper(height, idx, jdx)
                max_area = max(area, max_area)
        return max_area

class Solution:
    def helper(self,height, left, right):
        width = right - left
        height = min(height[left], height[right])
        area = width * height

        return area

    def maxArea(self,height):
        left = 0
        right = len(height)-1
        max_area = 0
        while (left<right):
            area = self.helper(height,left,right)
            max_area = max(max_area,area)
            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        return max_area



if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(Solution().maxArea(height))