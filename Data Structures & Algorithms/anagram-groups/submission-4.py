class Solution:
    def groupAnagrams(self, sts: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in sts:
            canonical = ''.join(sorted(word))
            anagram_groups[canonical].append(word)
        res = list(anagram_groups.values())
        return res


    
