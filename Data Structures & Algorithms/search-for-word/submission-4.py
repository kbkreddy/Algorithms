class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def getValidN(i,j, index, visited):
            res = []
            n = [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]

            for (x,y) in n:
                if 0<=x<len(board) and 0<=y<len(board[0]) and (x,y) not in visited:
                    if board[x][y] == word[index]:
                        res.append((x,y))
            return res        
        
        def dfs(i,j,visited):

            q = deque()
            visited.add((i,j))
            q.append((i,j,1,visited))
            while q:
                currI, currJ , index,visited = q.popleft()
                newVisited = visited.copy()
                if index >=len(word):
                    return True
                temp = getValidN(currI,currJ, index, newVisited)
                for x in temp:
                    newVisited.add((x[0],x[1]))
                    q.append((x[0],x[1],index+1,newVisited.copy()))
                    newVisited.remove((x[0],x[1]))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if dfs(i,j, set()):
                        return True
        return False
        


 
                

                

                



            
        