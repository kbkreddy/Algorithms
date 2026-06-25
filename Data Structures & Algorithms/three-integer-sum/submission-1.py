class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = set()
        i=0
        while i<len(nums)-2:
            target = nums[i]
            j=i+1
            k=len(nums)-1
            while(k>j):
                if nums[k]+nums[j]== target*-1:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[k]+nums[j]>target*-1:
                    k-=1
                else:
                    j+=1
            i+=1
        return list(map(lambda x:list(x),res))










        