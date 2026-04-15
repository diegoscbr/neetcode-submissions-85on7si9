class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            m = start + (end-start) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                start = m + 1
            elif nums[m] > target:
                end = m  - 1
        return -1
