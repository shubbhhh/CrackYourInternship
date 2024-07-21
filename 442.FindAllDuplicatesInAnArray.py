class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashset = set()
        res = []
        for i in nums:
            if i in hashset:
                res.append(i)
            # hashset[i] = 1 + hashset.get(i, 0)
            else:
                hashset.add(i)

        return res