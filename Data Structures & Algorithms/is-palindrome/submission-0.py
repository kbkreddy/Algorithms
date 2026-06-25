class Solution:
    def isPalindrome(self, s: str) -> bool:

        validVal = ''

        for ch in s:
            if ch.isalnum():
                validVal+=ch.lower()
        
        return validVal==validVal[::-1]
        