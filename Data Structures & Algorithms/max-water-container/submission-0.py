class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        #keep the max stored and iterate two pointers 
        #until the pointers  dont intersect
        length = len(heights)
        for i, bar in enumerate(heights):
            j = i
            k = len(heights) - 1

            while j < length - 1 and k >= 0: 
                if heights[j] < heights[k]:
                    #check max area, if bigger, update
                    area = (k-j) * min(heights[j], heights[k])
                    maxArea = max(maxArea, area)
                    j += 1
                if heights[k] < heights[j]:
                    area = (k-j) * min(heights[j], heights[k])
                    maxArea = max(maxArea, area)
                    k -= 1
                
                if heights[k] == heights[j]:
                    area = (k-j) * min(heights[j], heights[k])
                    maxArea = max(maxArea, area)
                    k -= 1
                    j+= 1


            return maxArea