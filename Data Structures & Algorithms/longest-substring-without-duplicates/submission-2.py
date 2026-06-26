class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i =0
        j = 0
        uniq = set()
        maxi = 0
        if len(s)==0:
            return 0
        while j<=len(s)-1:
            if s[j] not in uniq:
                maxi = max( maxi, j-i)
                uniq.add(s[j])
                j+=1
            else: 
                while s[j] in uniq:
                    uniq.remove(s[i])
                    i+=1
            
        return maxi+1
                


        