class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        window = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        for c in s:
            if c in window:
                if stack and stack[-1] == window[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
    