class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #store list of numbs into a dictionary 
        numStore = {}
        for num in nums:
            if num not in numStore: 
                numStore[num] = 0
            if num in numStore:
                numStore[num] += 1
       
       #now loop through map and check for the k  higest frequency numbers
       
       #init list 
        resList = [] 
        i = 0
        while i < k:
            maxValKey = max(numStore, key=numStore.get)
            if maxValKey in numStore:
                resList.append(maxValKey)
            numStore.pop(maxValKey, numStore[maxValKey])
            i +=1
        return resList
        
            
