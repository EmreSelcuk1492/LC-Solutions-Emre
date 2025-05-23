#racecar
#racecar 
#F_____L
#F == L
#
#1 - R = R
#2 - A = A
#3 - C = C
#Pointer in the front and back move sycnrhonesouly
#If it is odd, middle value doesn't count

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        for i in range(0, len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
