class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # result array starts with all 0s
        # if no warmer temperature exists, answer stays 0
        result = [0] * len(temperatures)

        # stack stores INDEXES of temperatures
        # these indexes are still waiting for a warmer day
        stack = [] 

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result