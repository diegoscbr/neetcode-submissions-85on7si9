class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #write out the three cases: sum too small, sum too big, sum equals target.
        
        i, j = 0, len(numbers)-1
        while i <= len(numbers)-1 and j > 0 and i != j:
            #too small
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1
            
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]

        

            