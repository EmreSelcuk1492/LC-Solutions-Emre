#{'r': 2, 'a': 2, 'c': 2, 'e': 1}
IsAnagram:
1 Dictioanry (Adding the letters of the first word, subtracting and seeing if we hit exactly perfect amount of collisions)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        if len(t) != len(s):
            return False

        else:
            for c in s:
                if c in myDict:
                    myDict[c] +=1
                else:
                    myDict[c] = 1

            for c in t:
                if c in myDict and myDict[c] > 0:
                    myDict[c] -= 1
                else:
                    return False
            print(myDict)
            return True
        
