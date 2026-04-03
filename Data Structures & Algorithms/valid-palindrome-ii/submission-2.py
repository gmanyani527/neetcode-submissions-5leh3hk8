class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(left, right): 
            while left < right: 
                if s[left] != s[right]: 
                    return False
                else: 
                    left += 1
                    right -= 1
            return True
            
        left, right = 0, len(s) - 1 

        while left < right: 
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum(): 
                right -= 1
            if s[left] != s[right]: 
               return is_palindrome(left + 1, right) or is_palindrome(left, right-1)
            else: 
                left += 1
                right -= 1
        return True