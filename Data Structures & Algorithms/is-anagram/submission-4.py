class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        #create a set of seen characters
        seen1 = set()
        hashMap1 = {}
        #create a dict and push to dct 
        for char in s:
            if char not in seen1:
                seen1.add(char)
                hashMap1[char] = len(char)
            elif char in seen1:
                hashMap1[char] += 1 
                
        seen2 = set()
        hashMap2 = {}
        for char in t:
            if char not in seen2:
                seen2.add(char)
                hashMap2[char] = len(char)
            elif char in seen2:
                hashMap2[char] += 1
        res = []
        for key in list(hashMap1):
            if key not in hashMap2:
                return False
            
            if  hashMap1[key] == hashMap2[key]:
                res.append(1)
            elif hashMap1[key] != hashMap2[key]:
                res.append(-1)

        if -1 not in res:
            return True
        else: return False


        
        




        