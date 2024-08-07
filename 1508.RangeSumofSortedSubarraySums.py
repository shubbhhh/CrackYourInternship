class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumArr = []
        for i in range(len(nums)):
            sum_ = 0
            for j in range(i, len(nums)):
                sum_ += nums[j]
                sumArr.append(sum_)

        sumArr.sort()

        range_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            range_sum = (range_sum + sumArr[i]) % mod
        
        return range_sum