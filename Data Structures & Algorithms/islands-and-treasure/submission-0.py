class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        rows = len(grid)
        columns = len(grid[0])

        q = deque()
        visit = set()

        def addCell(r,c):
            if (min(r,c)<0 or r == rows or c ==columns or (r,c) in visit or grid[r][c]==-1):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                grid[curr[0]][curr[1]]  = dist
                for newr,newc in directions:
                    addCell(curr[0]+newr,curr[1]+newc)

            dist+=1

            

        return
        


            
        