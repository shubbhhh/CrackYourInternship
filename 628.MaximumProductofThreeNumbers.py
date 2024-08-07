class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # max_prod = float("-inf")

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             max_prod = max(max_prod, nums[i]*nums[j]*nums[k])
        # nums.sort()
        # max_prod = nums[-1]*nums[-2]*nums[-3]
        # return max_prod

        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])