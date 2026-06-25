from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = defaultdict(int)

        for i in range(len(nums)):
            if target-nums[i] in cache:
                return [cache[target-nums[i]],i]
            else:
                cache[nums[i]] = i

        
        