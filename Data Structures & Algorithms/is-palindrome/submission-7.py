class Solution:
    def isPalindrome(self, s: str) -> bool:
        #iseven then l = len //2 r = l + 1
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        length = len(s) - 1
        if len(s) % 2 == 0:
            l = (length // 2)
            r = l + 1
            while l > -1 and r <= length:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    return False
            return True
        elif len(s) % 2 != 0:
            l, r = length // 2, length // 2
            while l > -1 and r <= length:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    return False
            return True
