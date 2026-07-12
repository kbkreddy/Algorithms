class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        vals = set(nums)
        def dfs(vals, currList):

            if not vals:
                res.append(currList)
            
            temp = set(vals.copy())
            for x in vals:
                newList = currList[:]
                temp.remove(x)
                newList.append(x)
                dfs(temp, newList)
                temp.add(x)

        dfs(nums,[])    
        return res





        
        