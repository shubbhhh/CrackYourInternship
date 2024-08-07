class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = nums.count(1)
        max_ones = curr_cnt = sum(nums[:k])

        for i in range(k, n + k):
            curr_cnt += nums[i % n]
            curr_cnt -= nums[(i - k + n) % n]
            max_ones = max(max_ones, curr_cnt)

        return k - max_ones