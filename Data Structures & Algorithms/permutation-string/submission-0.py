import numpy as np
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [0]*26
        counts2 = [0]*26

        for ch in s1:
            val = ord(ch) - 97
            counts1[val]+=1
        i = 0 
        while i< len(s2):
            val = ord(s2[i]) - 97
            if i-len(s1)>=0:
                counts2[ord(s2[i-len(s1)])-97]-=1
            counts2[val]+=1
            if(np.array_equal(counts1,counts2)):
                return True
            i+=1

        return False


        