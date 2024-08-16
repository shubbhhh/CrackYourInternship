class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        curr = 0
        for i in nums:
            curr += i
            self.sums.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        rsum = self.sums[right]
        lsum = self.sums[left - 1] if left > 0 else 0
        return rsum - lsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)