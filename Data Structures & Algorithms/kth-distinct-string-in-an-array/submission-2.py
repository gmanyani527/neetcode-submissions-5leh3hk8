class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {} 
        for word in arr: 
            if word in freq: 
                freq[word] += 1
            else: 
                freq[word] = 1
        for word in freq: 
            if freq[word] == 1: 
                k -= 1
                if k == 0:
                    return word
        return ""