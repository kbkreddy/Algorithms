class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res = [[]]


        for x in nums:
            temp = []
            for arr in res:
                new = arr[:]
                new.append(x)
                temp.append(new)
            if temp:
                res.extend(temp)
        return res
                
        