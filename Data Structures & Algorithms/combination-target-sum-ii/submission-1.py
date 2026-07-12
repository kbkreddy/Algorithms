class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = set()

        def dfs(nums, curr,target):

            if target == 0:
                res.add(tuple(curr))
                return
            elif target<0:
                return
            if nums:
                newList = curr[:]
                newList.append(nums[0])
                currVal = nums[0]
                if currVal <= target:
                    dfs(nums[1:],newList, target - currVal)
                if nums and nums[0]==currVal:
                    
                    while nums and nums[0]==currVal:
                        nums = nums[1:]
                    dfs(nums, curr, target)
                    
                else:
                    dfs(nums[1:], curr, target)

        dfs(candidates, [], target)

        return [list(x) for x in res]
        