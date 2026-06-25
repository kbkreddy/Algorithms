class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        cache = set()
        for x in nums:
            if x in cache:
                return True
            else:
                cache.add(x)

        return False
        