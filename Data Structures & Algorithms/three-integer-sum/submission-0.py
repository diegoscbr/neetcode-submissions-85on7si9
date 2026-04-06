class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordered = sorted(nums)
        length = len(ordered)
        res = set()

        for k in range(1, length - 1):  # fix the middle element
            i, j = 0, length - 1

            while i < k and j > k:      # left pointer left of k, right pointer right of k
                total = ordered[i] + ordered[k] + ordered[j]

                if total == 0:
                    res.add((ordered[i], ordered[k], ordered[j]))
                    i += 1
                    j -= 1
                elif total < 0:
                    i += 1
                else:
                    j -= 1

        return [list(t) for t in res]
        



