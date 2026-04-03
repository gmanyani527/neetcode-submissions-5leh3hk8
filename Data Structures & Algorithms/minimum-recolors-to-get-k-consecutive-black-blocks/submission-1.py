class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        write = 0
        for i in range(k):
            if blocks[i] == 'W':
                write += 1
        ans = write

        for next in range(k, len(blocks)):
            if blocks[next] == 'W':
                write += 1
            if blocks[next - k] == 'W':
                write -= 1
            ans = min(ans, write)
        return ans

