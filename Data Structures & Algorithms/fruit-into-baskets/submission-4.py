class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {} 
        left = 0
        count = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit in window:
                window[fruit] += 1
            else: 
                window[fruit] = 1
            
            while len(window) > 2: 
                left_fruit = fruits[left]
                window[left_fruit] -= 1
                if window[left_fruit] == 0:
                    del window[left_fruit]
                left += 1 
            count = max(count, right - left + 1)
        return count
            
