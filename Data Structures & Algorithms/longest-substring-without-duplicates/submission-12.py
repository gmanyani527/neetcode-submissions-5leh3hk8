class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        count = 0

        for char in range(len(s)):
            while s[char] in window:
                window.remove(s[left])
                left += 1
            count = max(count, char - left + 1 )
            window.add(s[char])
             
        return count  


        