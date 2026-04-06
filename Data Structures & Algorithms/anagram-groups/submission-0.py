class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        print(res)
        for s in strs:
            sortedS = ''.join(sorted(s))
            print(sortedS)
            res[sortedS].append(s)
        res2 = list(res.values())
        return res2
        
        
