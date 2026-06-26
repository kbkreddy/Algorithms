class Solution:
    def maxProfit(self, p: List[int]) -> int:

        i = len(p)-2
        prof = 0
        maxi = p[len(p)-1]
        while i>=0:
            print(i)
            curr = maxi - p[i]
            if (curr > prof):
                prof = curr 
            
            if (p[i]>maxi):
                maxi = p[i]
            i-=1
        return prof




        