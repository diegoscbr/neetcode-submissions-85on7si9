class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

        The output should not contain any duplicate triplets. You may return the output and the triplets in any order."""
        """Input: nums = [-1,0,1,2,-1,-4]

        Output: [[-1,-1,2],[-1,0,1]]"""
        ordered = sorted(nums)
        print(ordered)
        length = len(nums)
        i =0
        res = []
        for i, num in enumerate(ordered):
            if i > 0 and ordered[i] == ordered[i - 1]:
                continue
            target = -ordered[i]
            j, k = i + 1, length-1
            ordered[j:k]
            while j < k: 
                if ordered[j] + ordered[k] > target:
                    k -= 1
                elif ordered[j] + ordered[k] < target:
                    j += 1
                elif ordered[j] + ordered[k] == target:
                    result = [ordered[i], ordered[j], ordered[k]]
                    res.append(result)
                    while j < k and ordered[j] == ordered[j + 1]:
                        j += 1
                    while j < k and ordered[k] == ordered[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res


