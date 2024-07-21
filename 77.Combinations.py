class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(lst, start):
            # base case
            if len(lst) == k:
                res.append(lst[:])
                return 
            else:    
                for i in range(start, n+1):
                    # updating the state
                    lst.append(i)

                    helper(lst, i+1)

                    # restoring the state
                    lst.pop()
        res =[]
        helper([], 1)

        return res