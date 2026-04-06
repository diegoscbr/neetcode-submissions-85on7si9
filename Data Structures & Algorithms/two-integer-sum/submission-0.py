class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        #shoulf have the key be the value, and value be index
        #ex: diffMap[num] = i
        #populate chart with differences

        for i, num in enumerate(nums):
            cur = nums[i]
            diff = target - cur
            if diff in diffMap:
                return [diffMap[diff], i]
            if diff not in diffMap:
                diffMap[num] = i
        
        print(diffMap)
                
