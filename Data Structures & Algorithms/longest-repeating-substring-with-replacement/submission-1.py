class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        left = 0
        maxF = 0
        res = 0

        #we need to make a hashmap for each char count
        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else: 
                count[char] = 1
            
            if count[char] > maxF: 
                maxF = count[char]
            while (right - left + 1) - maxF > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            window_size = right - left + 1
            if window_size > res: 
                res = window_size
        return res
        # then we compare it with the other maxF 

        # and then if there is a chance we must then update the maxF
        # by subtracting right - left + 1 - maxF >= k which