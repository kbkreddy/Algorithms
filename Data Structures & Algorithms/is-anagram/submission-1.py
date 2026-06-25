from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for x in s:
            countS[x]+=1
        for y in t:
            countT[y]+=1
        if len(countS)!=len(countT):
            return False
        for values in list(countS.items()):
            print(str(values[0]))
            if countT[values[0]]==values[1]:
                continue
            else:
                return False
        return True



        