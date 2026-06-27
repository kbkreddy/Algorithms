class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        dic = defaultdict(int)

        i=0
        j=0
        maxf = 0 
        res = 0 
        while j<len(s):

            dic[s[j]]+=1
            if maxf<dic[s[j]]:
                maxf = dic[s[j]]
            while(j-i+1 - maxf) > k:
                dic[s[i]] -=1
                i+=1
            print(maxf, res , dic.items())
            if res < j-i+1:
                res = j-i+1
            j+=1
            

        return res