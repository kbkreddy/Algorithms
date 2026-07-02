class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        

        res = [0]*len(t)
        stack = []
        i = 0 
        while i<len(t):
            if not stack:
                stack.append([t[i],i])
            else:
                if stack[-1][0] > t[i]:
                    stack.append([t[i],i])
                else:
                    while stack and stack[-1][0]<t[i]:
                        prevTemp, prevIndex = stack.pop()
                        diff = i - prevIndex
                        res[prevIndex] = diff
                    stack.append([t[i],i])
            i+=1
        return res


