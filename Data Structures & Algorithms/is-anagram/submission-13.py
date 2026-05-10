class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {} #letter : frequency

        for i, letter in enumerate(s):
            if s[i] not in seen:
                seen[s[i]] = 1
            elif s[i] in seen:
                seen[s[i]] += 1
        print(seen)
        for i, letter in enumerate(t):
            if t[i] not in seen:
                return False
            elif t[i] in seen:
                seen[t[i]] -= 1
        
        vals = seen.values()
        for val in vals:
            if val > 0:
                return False
        return True

        
            
            

        