class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # result array starts with all 0s
        # if no warmer temperature exists, answer stays 0
        result = [0] * len(temperatures)

        # stack stores INDEXES of temperatures
        # these indexes are still waiting for a warmer day
        stack = []

        # loop through temperatures with index and value
        for i, temp in enumerate(temperatures):

            # while:
            # 1. stack is not empty
            # 2. current temperature is warmer than stack top temperature
            while stack and temperatures[stack[-1]] < temp:

                # remove previous index from stack
                prev_index = stack.pop()

                # calculate how many days waited
                # current index - previous index
                result[prev_index] = i - prev_index

            # push current index onto stack
            # this temperature is now waiting for a warmer day
            stack.append(i)

        return result