class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        write = 0
        for i in range(k):
            if blocks[i] == 'W':
                write += 1
        ans = write
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                write += 1
            if blocks[i-k] == 'W': 
                write -= 1
            ans = min(ans, write)
        return ans






































