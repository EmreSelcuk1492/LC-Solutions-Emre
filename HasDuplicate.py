Has Dupicate -> First Try

Description: Used dictionary as a way to track collisions.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict={}
        for i in nums:
            if i in myDict:
                return True
            else:
                myDict[i] = 0
        return False
         
