import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """If we get the prefix products arr and 
        the suffix arr t
        heir products are the combination"""

        #EX nums = [1, 2, 4, 6]
        # PREFIX = [NONE, 1, 2, 8]
        # SUFFIX = [48, 24, 6, NONE]
        # PRE*SUF = [48, 24, 12, 8]
        preProds = []
        sufProds = []
        for i, num in enumerate(nums):
            prefix = nums[:i]
            suffix = nums[i+1:]
            #case where there is no prefixes
            if not prefix:
                preProds.append(1)

            #now muliply
            if prefix: 
                temp_prod = math.prod(prefix)
                preProds.append(temp_prod)
            if suffix:
                temp_prod = math.prod(suffix)
                sufProds.append(temp_prod)
            if not suffix: 
                sufProds.append(1)
        
        
        print(f"pre:{preProds}, suf:{sufProds}")
            
        res = [a*b for (a, b) in zip(preProds, sufProds)]    
        return res   



