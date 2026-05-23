class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        area = 0
        l = 0
        r = n-1

        for i in range(n):
            area = (r - l) * (min(heights[l],heights[r]))
            maxArea = max(area, maxArea)

            if(heights[l] < heights[r]):
                l += 1
            elif(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
                r -= 1

        return maxArea
        