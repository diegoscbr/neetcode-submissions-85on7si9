class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i, num in enumerate(numbers):
            j = i
            k = length - 1
            while j < k:
                if numbers[j] + numbers[k] > target:
                    k -=1
                if numbers[j] + numbers[k] < target:
                    j +=1
                if numbers[j] + numbers[k] == target:
                    return [j+1, k+1]
