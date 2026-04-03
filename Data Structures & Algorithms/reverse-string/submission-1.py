class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        We need to traverse this from the front and back 
        taking the letters that we find in the front pointer
        to the back. we could copy this to a new whole array
        but that would mean taking up more space. so its better
        to do it using two pointers. from the examples it is not 
        including spaces so that check is not needed. 
        """
        right, left = 0, len(s) - 1

        while right < left: 
            s[right],s[left] = s[left], s[right]
            right += 1
            left -= 1 
        
