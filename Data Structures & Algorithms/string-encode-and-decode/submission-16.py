class Solution:
    def encode(self, strs: List[str]) -> str:
        deliminator = "漢"
        res = ""
        for s in strs:
            res += s
            res += deliminator
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        deliminator = "漢"
        res = []
        start = 0
        for i in range(len(s)):
            if s[i] == deliminator:
                res.append(s[start:i])
                start = i + 1

        print(res)
        return res