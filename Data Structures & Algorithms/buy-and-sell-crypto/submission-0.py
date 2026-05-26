class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxList = [0] * len(prices)

        curr = 0
        r = 1

        for i, p in enumerate(prices):
            r = i+1
            while r < len(prices):
                diff = prices[r] - prices[i]
                maxList[i] = max(diff, maxList[i])
                r +=1
            i+=1
        return max(maxList)
                    

        
