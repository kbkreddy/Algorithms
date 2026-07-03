class Solution:
    def search(self, nums: List[int], target: int) -> int:


        i =0 
        j = len(nums)-1

        while i<j:

            mid = (i+j)//2

            if nums[mid] > nums[j]:
                i = mid +1
            else:
                j = mid
        small = i
        if target > nums[len(nums)-1]:
            i =0
            j = small-1
        else:
            i=small
            j = len(nums)-1
        
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j= mid -1
            else:
                i = mid +1
        return -1
        

