class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        rows = len(grid)
        columns = len(grid[0])

        maxIsland = 0


        def dfs(r,c,area):

            if r<0 or r>=rows or c<0 or c>=columns or grid[r][c]==0:
                return area

            area+=1
            grid[r][c] = 0

            for newr,newc in directions:
                area+=dfs(r+newr,c+newc,0)
            
            return area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1:
                    curr = dfs(r,c,0)
                    print(curr)
                    if curr>maxIsland:
                        maxIsland = curr
        return maxIsland
