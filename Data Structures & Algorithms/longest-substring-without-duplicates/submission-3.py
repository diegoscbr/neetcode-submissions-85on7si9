class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengths = []

        i, r = 0, 0
        if not s: return 0
        while r < len(s):
            
            if len(set(s[i:r+1])) == len(s[i:r+1]):
                print(f"Window: {set(s[i:r+1])}")
                lengths.append(len(s[i:r+1]))
                r+= 1
            else:
                
                i += 1
        print(lengths)
        return(max(lengths))
                

