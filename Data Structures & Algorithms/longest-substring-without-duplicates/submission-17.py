class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        window = set()
        left = 0 

        for i in range(len(s)):
            while s[i] in window: 
                window.remove(s[left])
                left += 1
            window.add(s[i])
            length = max(length, i - left + 1)
        return length
