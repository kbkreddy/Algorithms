class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        i = 0
        j = len(matrix)-1

        while i<=j:

            mid = (i+j)//2
            curr = matrix[mid][0] 
            if curr == target:
                return True
            elif curr > target:
                j = mid - 1
            else:
                i = mid+1
            
        frow = j
        i =0
        j = len(matrix[0])-1

        while i<=j:
            mid = (i+j)//2
            curr = matrix[frow][mid]

            if curr ==  target:
                return True
            elif curr > target:
                j= mid -1
            else:
                i = mid +1

        return False

        