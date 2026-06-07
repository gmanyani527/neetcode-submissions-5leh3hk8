from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        largestOdd = 0
        smallestEven = float('inf')

        for count in freq.values():
            if count % 2 == 1:
                largestOdd = max(largestOdd, count)
            else:
                smallestEven = min(smallestEven, count)

        return largestOdd - smallestEven