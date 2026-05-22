class Solution:
    def isValid(self, s: str) -> bool:
        window = {']':'[', '}':'{', ')':'('}
        stack = []
        
        for char in s: 
            if char in window: 
                if stack and stack[-1] == window[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
