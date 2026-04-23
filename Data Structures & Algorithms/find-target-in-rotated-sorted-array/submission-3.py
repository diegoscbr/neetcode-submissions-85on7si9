class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Phase 1: find the rotation breakpoint (index of the minimum)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1      # min is in the right half
            else:
                r = m          # min is at m or in the left half

        pivot = l  # index of the smallest element

        # Phase 2: binary search the correct half
        if target >= nums[pivot] and target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1