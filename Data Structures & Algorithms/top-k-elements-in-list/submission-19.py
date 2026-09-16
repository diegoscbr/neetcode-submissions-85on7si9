class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            if num not in freq:
                freq[num] = 1
            elif num in freq:
                freq[num] += 1
        freq = dict(freq)
        sorted_dict = sorted(freq.items(), key=lambda item: item[1], reverse= True)

        i = 0
        res = []
        while i <= k-1:
            res.append(sorted_dict[i][0])
            i+= 1
        return res

            
        

