class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = float("-inf")
        prevMin, prevMax = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, prevMax - arrays[i][0], arrays[i][-1] - prevMin)
            prevMin, prevMax = min(prevMin, arrays[i][0]), max(prevMax, arrays[i][-1])

        return res