class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i, num in enumerate(nums):
            if (nums[i] - 1) not in numSet:
                length = 0
                while (nums[i] + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

 