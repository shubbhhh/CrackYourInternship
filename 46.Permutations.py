class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def helper(nums, index):
            nonlocal permutations
            if index == (len(nums)-1):
                permutation = []
                for i in nums:
                    permutation.append(i)
                # print("nums:", nums, "index:", index, "permutation:", permutation)
                permutations.append(permutation)
            else:
                for i in range(index, len(nums)):
                    nums[i], nums[index] = nums[index], nums[i]
                    helper(nums, index+1)
                    nums[i], nums[index] = nums[index], nums[i]

        helper(nums, 0)
        return permutations