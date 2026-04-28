class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        maxF = 0        
        window_size = 0


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
            if (right - left + 1) > window_size:
                window_size = right - left + 1
        return window_size
            


            
