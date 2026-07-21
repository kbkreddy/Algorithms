class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        q  =deque()

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def addCell(r,c):
            if r<0 or r==rows or c<0 or c==cols or (r,c) in visit or grid[r][c]== 0:
                return

            visit.add((r,c))
            q.append([r,c])

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        maxDist = 0 
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                r = curr[0]
                c = curr[1]

                grid[r][c] = 2

                for newc,newr in directions:
                    addCell(newr+r,newc+c)
                
            maxDist = max(maxDist,dist)
            dist+=1

        print(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return maxDist



        