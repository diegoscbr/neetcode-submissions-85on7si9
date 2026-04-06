class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        seen = {}
        #diff is what we are checking against
        #we are storing index: value in seen at each num
        for i,  num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        

        
        
            

            
            