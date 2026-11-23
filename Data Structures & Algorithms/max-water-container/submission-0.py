class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l < r:
            dist = r - l 
            maxWater = max(maxWater, min(heights[l], heights[r]) * dist)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
            


    #calc max amount of water each pass
    #   dist = r - l
    #   maxWater = min(heights[l], heights[r]) * dist
