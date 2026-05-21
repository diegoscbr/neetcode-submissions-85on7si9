class Solution:

    def encode(self, strs: List[str]) -> str:
        delim = "$"
        res = ""
        for s in strs:
            length = str(len(s))
            res += length + delim + s
        return res

        

    def decode(self, s: str) -> List[str]:
        delim = "$"
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != delim:
                j += 1
            length = int(s[i:j])
            temp = s[j+1: j+1+length]
            res.append(temp)
            i = j + 1 + length
        return res

            
