class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(sub, index):
            if index == len(nums):
                if sorted(sub) not in res:
                    res.append(sorted(sub[:]))
                return

            helper(sub, index + 1)

            sub.append(nums[index])
            helper(sub, index + 1)
            sub.pop()

        res = []
        helper([], 0)
        return res
            
            