class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_h = 0
        max_height = 0
        for i in range(len(gain)):
            curr_h += gain[i]
            max_height = max(max_height, curr_h)

        return max_height