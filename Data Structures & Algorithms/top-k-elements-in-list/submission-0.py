class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = defaultdict(int)

        for x in nums:
            cache[x]+=1

        arrayCount = list(cache.items())

        arrayCount.sort(key=lambda x:x[1], reverse = True)

        res = []

        for item in arrayCount[:k]:
            res.append(item[0])

        return res
        
        
        