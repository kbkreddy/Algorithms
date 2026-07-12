class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = set()

        def dfs(nums, curr,target):

            if target == 0:
                res.add(tuple(curr))
            elif target<0:
                return
            if nums:
                newList = curr[:]
                newList.append(nums[0])
                dfs(nums,newList, target - nums[0])
                dfs(nums[1:], curr, target)
        dfs(nums, [], target)

        return [list(x) for x in res]