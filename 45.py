class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = len(nums) - 1
        nums[target] = 0
        for i_0 in range(target-1, -1, -1):
            if nums[i_0] == 0:
                nums[i_0] = sys.maxsize
                continue
            distance = nums[i_0]
            if target - (i_0 + distance) < 0:
                nums[i_0] = 1
            else:
                i_1 = i_0 + 1
                nums[i_0] = 1 + min(nums[i_1:i_1+distance])
        return nums[0]
