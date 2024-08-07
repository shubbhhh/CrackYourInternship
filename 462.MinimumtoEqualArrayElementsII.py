class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[(len(nums)-0)//2]
        moves = 0

        for i in range(len(nums)):
            if nums[i] < mid:
                moves += mid - nums[i]
            else:
                moves += nums[i] - mid

        return moves