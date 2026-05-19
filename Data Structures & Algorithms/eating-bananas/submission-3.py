class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        mini = right

        while left <= right: 
            hours = 0
            k = (left + right) // 2 
            for p in piles: 
                hours += math.ceil(p/k)
            if hours <= h: 
                mini = min(mini,k)
                right = k - 1
            else:
                left = k + 1
        return mini
