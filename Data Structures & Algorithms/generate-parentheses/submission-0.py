class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        oc = 0
        cc = 0

        def dfs(subset, oc, cc):
            if cc > oc or cc >n or oc > n:
                return
            if oc == n and cc ==n:
                if subset:
                    res.append(subset)
                return
            subset+='('
            oc+=1
            dfs(subset,oc,cc)
            subset=subset[:-1]
            oc-=1
            subset+=')'
            cc+=1
            dfs(subset, oc,cc)
        
        dfs('',0,0)
        return res

            
        