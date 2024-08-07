class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        endIntv = intervals[0][1]
        res = 0

        for i in intervals[1:]:
            if i[0] >= endIntv:
                endIntv = i[1]
            else:
                res += 1
                endIntv = min(endIntv, i[1])

        return res