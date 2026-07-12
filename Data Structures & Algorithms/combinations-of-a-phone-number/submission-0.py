class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        dic = defaultdict(str)
        dic["2"] = 'abc'
        dic["3"] = 'def'
        dic["4"] = 'ghi'
        dic["5"] = 'jkl'
        dic["6"] = 'mno'
        dic["7"] = 'pqrs'
        dic["8"] = 'tuv'
        dic["9"] = 'wxyz'
        
        def dfs(digits, subset):

            if not digits:
                if subset:
                    res.append(subset)
                return

            digitChars = dic[digits[0]]

            for char in digitChars:
                subset+=char
                dfs(digits[1:], subset )
                subset = subset[:-1]
        dfs(digits, '')

        return res






        