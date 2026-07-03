class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        maxi = 0

        for b in piles:
            maxi = max(maxi,b)
        
        i = 1 
        j = maxi
        while i<=j:

            mid = (i+j)//2
            if self.gethrs(piles, mid) > h:
                i = mid +1
            else:
                j = mid - 1
        return j+1



    def gethrs(self, piles, sp):

        sum = 0
        for p in piles:
            sum+= math.ceil(p/sp)
        return sum


        