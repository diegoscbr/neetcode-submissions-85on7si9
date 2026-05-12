class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        canonical_s = ''.join(sorted(s))
        canonical_t = ''.join(sorted(t))
        if canonical_s == canonical_t:
            return True
        return False