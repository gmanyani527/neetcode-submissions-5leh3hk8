class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            if fruit in baskets:
                baskets[fruit] += 1
            else: 
                baskets[fruit] = 1
            
            
            while len(baskets) > 2: 
                left_fruit = fruits[left]
                baskets[left_fruit] -= 1 
                if baskets[left_fruit] == 0:
                    del baskets[left_fruit]
                left += 1 
            max_len = max(max_len, right - left + 1)
        return max_len
            
