class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in range(len(details)):
            if (details[i][11] + details[i][12]) > "60":
                res += 1

        return res