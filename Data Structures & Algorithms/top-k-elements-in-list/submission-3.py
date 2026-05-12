class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} #num: freq
        for num in nums:
            if num in seen:
                seen[num] += 1
            elif num not in seen:
                seen[num] = 1
        sortedSeen = sorted(seen.items(), key = lambda item: item[1], reverse=True)
        print(sortedSeen)
        res = []
        for item in sortedSeen: 
            
            if k >0:
                res.append(item[0])
                print(res)
                k-= 1
        return res


            