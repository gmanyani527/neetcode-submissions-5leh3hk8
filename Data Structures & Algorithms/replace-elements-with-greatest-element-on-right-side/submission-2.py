class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        have to make the last character -1
        and make thes ones after that increasing
        could traverse from the back but im forgetting
        how to place the -1
        '''
        n = len(arr)
        result = [0] * n
        rightMax = -1 
        for i in range(n-1, -1, -1):
            result[i] = rightMax 
            rightMax = max(arr[i], rightMax)
        return result