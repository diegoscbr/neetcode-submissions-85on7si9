from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #init dict
        subsequences = []
        longest = 0
        numSet = set(nums)
        for i, item in enumerate(nums):
            if (nums[i] - 1) not in numSet:
                length = 0
                while (nums[i] + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

                
         
