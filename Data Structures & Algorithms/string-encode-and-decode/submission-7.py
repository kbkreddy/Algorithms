class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for val in strs:
            res+=str(len(val))
            res+='#'
            res += val
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        cache = ''
        i=0 
        while(i<len(s)):
            lenChar = ''
            while s[i]!='#':
                lenChar+=s[i]
                i+=1
            
            lenS = int(lenChar)
            i+=1
            for y in range(i, i + lenS):
                cache+=s[y]
            res.append(cache)
            cache=''
            i+=lenS
        return res
