class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i= 0 
        j=len(numbers)-1

        while i<j:
            if target - numbers[j]==numbers[i]:
                return [i+1,j+1]
            elif target - numbers[j]<numbers[i]:
                j-=1
                continue
            else:
                i+=1
        
        