class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}

        for num in nums2:

            while stack and stack[-1] < num:
                smaller = stack.pop()
                nextGreater[smaller] = num

            stack.append(num)

        while stack:
            nextGreater[stack.pop()] = -1

        answer = []

        for num in nums1:
            answer.append(nextGreater[num])

        return answer