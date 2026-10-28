class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt = {}
        for num in nums2:
            while stack and num > stack[-1]:
                nxt[stack.pop()] = num
            stack.append(num)
        return [nxt.get(num, -1) for num in nums1]