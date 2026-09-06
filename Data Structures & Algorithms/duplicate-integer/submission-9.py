class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = "hit" 
            elif num in lookup:
                return True
        return False