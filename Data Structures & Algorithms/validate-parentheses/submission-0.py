class Solution:
    def isValid(self, s: str) -> bool:
        para = {"(":")","[":"]","{":"}"}
        stack = []

        for char in s:
            if char in para:
                stack.append(char)
            elif not stack or para[stack[-1]] != char:
                return False
            else:
                stack.pop()
        return not stack
            



      


        