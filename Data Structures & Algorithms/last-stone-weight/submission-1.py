class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        s = [x * -1  for x in stones]
        heapq.heapify(s)
        
        while len(s)>1:
            top1 = heapq.heappop(s)
            top2 = heapq.heappop(s)
            if top1==top2:
                continue
            else:
                heapq.heappush(s, abs(top1-top2)*-1)
        if not s:
            return 0
        return heapq.heappop(s)*-1


