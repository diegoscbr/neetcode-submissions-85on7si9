class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '€'
        res = ''
        for s in strs:
            res = res + s
            res += delimiter
        print(res)
        return res




    def decode(self, s: str) -> List[str]:
        deliminator = '€'
        res = []
        i = 0
        start = 0
        while i < len(s):
            if s[i] == deliminator:
                temp = s[start:i]
                res.append(temp)
                start = i + 1

            i += 1
        print(res)

        
        return res

