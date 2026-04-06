import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        We can use the prefix and suffix technique. 
        First, we iterate from left to right and store the prefix 
        products for each index in a prefix array, excluding the 
        current index's number. Then, we iterate from right to left 
        and store the suffix products for each index in a suffix array, 
        also excluding the current index's number. Can you figure out 
        the solution from here?
        """
        prefix = []
        suffix = []
        for i, num in enumerate(nums):
            #looking at the numbers before the current index
            temp_pre = nums[:i]
            temp_suf = nums[i+1:]
            #if the list is not empty
            if not temp_pre:
                prefix.append(1)
            if temp_pre:
                prod = math.prod(temp_pre)
                prefix.append(prod)
            if temp_suf:
                prod = math.prod(temp_suf)
                suffix.append(prod)
            if not temp_suf:
                suffix.append(1)
        print(prefix)
        print(suffix)
        result = [a * b for a, b in zip(prefix, suffix)]
        return result
        

            

            
        
                    
                
            
            #prefix-->[index: value]-->suffix
        #print(f" {nums[:curIndex]}-->[{curIndex}: {nums[curIndex]}]--> {nums[curIndex+1:]}")
        #print(prefix)





