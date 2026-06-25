class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        lprod = []
        rprod = [1]*len(nums)

        for i in range(len(nums)):
            if i==0:
                lprod.append(nums[i])
            else:
                lprod.append(lprod[i-1]*nums[i])
        
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                rprod[i] = nums[i]
            else:
                rprod[i] = rprod[i+1]*nums[i]
    
        res =[]

        for i in range(len(nums)):

            left, right = 1, 1
            if i-1>=0:
                left = lprod[i-1]
            if i+1<len(nums):
                right = rprod[i+1]
            res.append(left * right)

        return res





