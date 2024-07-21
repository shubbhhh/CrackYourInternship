class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ansLst = []
        def helper(n, currLst):
            if n == len(nums):
                ansLst.append(currLst[:])
                return

            helper(n+1, currLst)

            currLst.append(nums[n])
            helper(n+1, currLst)
            currLst.pop()
        
        helper(0, [])
        return sorted(ansLst)