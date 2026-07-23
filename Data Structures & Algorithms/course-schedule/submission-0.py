class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReq = defaultdict(set)
        reverse = defaultdict(set)
        for x,y in prerequisites:
            preReq[x].add(y)
            reverse[y].add(x)    
        q = deque()

        for x in range(numCourses):
            if x not in preReq:
                q.append(x)
        while q:
            curr = q.popleft()
            for x in reverse[curr]:
                preReq[x].remove(curr)
                if not preReq[x]:
                    del preReq[x]
                    q.append(x)
            
        if not q and preReq:
            return False
        else:
            return True


        