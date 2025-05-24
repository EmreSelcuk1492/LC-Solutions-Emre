class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        temp = ""
        if len(s) < 2:
            return False

        for c in s:
            if c == "[" or c == "{" or c == "(":
                myStack.append(c)
            else:
                if len(myStack) != 0:
                    temp = myStack.pop()
                    print(temp)
                    print(c)
                    if (c == "]" and temp != "[") or (c == ")" and temp != "(") or (c == "}" and temp != "{"):
                        return False
                else:
                    return False
        if myStack:
            return False
        else:
            return True
