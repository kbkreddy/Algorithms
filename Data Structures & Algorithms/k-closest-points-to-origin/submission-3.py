class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        newList = [[x*x+y*y, x, y] for [x,y] in points ]
        heapq.heapify(newList)

        res = []
        print(newList)
        for i in range(k):
            [dist,i,j] = heapq.heappop(newList)
            res.append([i,j])
        return res