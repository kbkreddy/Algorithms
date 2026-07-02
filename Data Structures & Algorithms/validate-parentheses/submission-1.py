class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if self.isOpen(c):
                stack.append(c)
            else:
                if stack:
                    if stack[-1]==self.getOpen(c):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True



    
    def isOpen(self, s : str) -> bool:
        if s == "(" or s=="[" or s == "{":
            return True
        else:
            return False

    def getOpen(self, s: str) -> str:
        dic = defaultdict(str)
        dic[")"] = "("
        dic["}"] = "{"
        dic["]"] = "["
        return dic[s]




        