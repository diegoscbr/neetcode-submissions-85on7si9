import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(f"Input: {s}, with length: {len(s)}")
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        
        print(s)
        if len(s) % 2 == 0:
            length = len(s)
            median = length // 2
            r, l = median , median - 1
            while l >=0 and r < length:

                if s[l] != s[r]:
                    print("FALSE")
                    return False
                r += 1
                l -= 1
            print("TRUE")
            return True 

        if len(s) % 2 != 0: 
            length= len(s)
            median = length // 2
            l, r = median - 1 , median + 1
            while l >= 0 and r < len(s):
                print(s[l],s[r])
                if s[l] != s[r]:
                    print("FALSE")
                    return False
                l -= 1
                r +=1
            print("TRUE")
            return True

        return True