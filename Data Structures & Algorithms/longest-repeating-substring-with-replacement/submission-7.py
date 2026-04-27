class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        res = 0
        maxF = 0 


        for i in range(len(s)):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1 

            if window[s[i]] > maxF: 
                maxF = window[s[i]]
            while (i - left + 1) - maxF > k: 
                left_char = s[left]
                window[left_char] -= 1
                left += 1
            window_size = i - left + 1
            if window_size > res: 
                res = window_size
        return res 

