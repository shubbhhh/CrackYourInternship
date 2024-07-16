

def removeDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        curr = 0
        for i in nums:
            if i in seen:
                continue
            else:
                nums[curr] = i
                curr += 1
            seen.add(i)
        
        return len(set(nums))
