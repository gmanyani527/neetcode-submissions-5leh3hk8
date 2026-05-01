class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        left = 0
        window = {}
        maxF = 0


        for i in range(len(s)):
            right = s[i]
            if right in window:
                window[right] += 1
            else: 
                window[right] = 1
            
            if window[right] > maxF: 
                maxF = window[right]
            
            while (i - left + 1) - maxF > k: 
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1
            window_size = i - left + 1
            if window_size > count: 
                count = window_size
        return count