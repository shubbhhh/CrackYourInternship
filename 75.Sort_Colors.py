def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1

        for i in range(len(nums)):
            if i < zeros:
                nums[i] = 0
            elif zeros <= i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2
