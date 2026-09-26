class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif char == "C":
                stack.pop()
            elif char == "D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(char))
        return sum(stack)
