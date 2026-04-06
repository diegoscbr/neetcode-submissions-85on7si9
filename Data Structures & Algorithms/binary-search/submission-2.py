class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while end >= start:
            m =  start + (end - start) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                end = m -1 
            elif target > nums[m]:
                start = m + 1
        return -1
