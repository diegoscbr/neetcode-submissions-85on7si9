class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            canonical = ''.join(sorted(word))
            anagram_groups[canonical].append(word)
        res = list(anagram_groups.values())
        return(res)