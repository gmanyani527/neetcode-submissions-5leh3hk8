class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {} 
        res = 0
        left = 0
        maxF = 0

        for right in range(len(s)):
            char = s[right]
            if char in window:
                window[char] += 1
            else: 
                window[char] = 1 
            
            if window[char] > maxF:
                maxF = window[char]
            while (right - left + 1) - maxF > k:
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1
            window_size = right - left + 1
            if window_size > res:
                res = window_size
        return res