class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs: 
            length = len(word)
            result = result + str(length) + "#" + word
        return result
    def decode(self, s: str) -> List[str]:
        result = [] 
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1
            length_str = s[i:j]
            length = int(length_str)

            j += 1
            word = s[j:j + length]
            result.append(word)

            i = j + length
        return result