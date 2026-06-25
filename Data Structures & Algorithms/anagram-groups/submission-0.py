class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedStrings=[]
        for val in strs:
            sortedStrings.append([tuple(sorted(val)), val])
        
        cache = defaultdict(list)

        for sortedVal, val in sortedStrings:
            print(sortedVal)
            cache[sortedVal].append(val)
        
        return list(cache.values())
        