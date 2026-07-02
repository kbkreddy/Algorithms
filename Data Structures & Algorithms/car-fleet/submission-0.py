class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        tieArr = []

        i = 0

        while i< len(position):
            tieArr.append([position[i], (target - position[i])/speed[i]]) 
            i+=1  

        tieArr.sort(reverse= True)

        stack = []

        i = 0
        while i<len(tieArr):
            if not stack:
                stack.append(tieArr[i][1])
            elif tieArr[i][1] > stack[-1]:
                stack.append(tieArr[i][1])
            i+=1
        return len(stack)
        