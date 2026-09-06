class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        print(s)
        if len(s) <= 1:
            return True
        l, r = 0, len(s) - 1
        if s[l] == s[r]:
            s = s[l+1: r]
            return self.isPalindrome(s)
        return False
        