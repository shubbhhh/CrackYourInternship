class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = Counter(target)

        for i in arr:
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                del count[i]

        return True