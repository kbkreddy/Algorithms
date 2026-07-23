class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preReq = defaultdict(set)
        reverse = defaultdict(set)
        for x,y in prerequisites:
            preReq[x].add(y)
            reverse[y].add(x)    
        q = deque()
        
        for x in range(numCourses):
            if x not in preReq:
                q.append(x)
        print(preReq, reverse, q)
        while q:
            curr = q.popleft()
            res.append(curr)
            for x in reverse[curr]:
                preReq[x].remove(curr)
                if not preReq[x]:
                    del preReq[x]
                    res.append(x)
                    q.append(x)
        
        if not q and preReq:
            return []
        else:
            return res