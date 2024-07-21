class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(adds, start):
            print(adds)
            if sum(adds) > target:
                return
            if sum(adds) == target and adds not in res:
                res.append(adds[:])
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    if candidates[i] > target:
                        break
                    adds.append(candidates[i])
                    helper(adds, i + 1)
                    adds.pop()

        candidates.sort()
        res = []
        helper([], 0)
        return res
