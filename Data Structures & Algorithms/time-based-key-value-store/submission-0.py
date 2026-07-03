class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        sarr = self.hash[key]

        if not sarr:
            return ""

        i =0 
        j = len(sarr)-1

        while i<=j:
            mid = (i+j)//2
            curr = sarr[mid][1]
            if curr == timestamp:
                return sarr[mid][0]
            elif  curr > timestamp:
                j = mid -1
            else:
                i = mid +1
        if j >=0 and j<len(sarr):
            return sarr[j][0]
        return ""
        
        
