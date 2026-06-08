class Solution:
    def kthDistinct(self, arr: List[str], k: int):

        freq = {}

        for word in arr:
            freq[word] = freq.get(word, 0) + 1

        for word in arr:
            if freq[word] == 1:
                k -= 1

                if k == 0:
                    return word

        return ""