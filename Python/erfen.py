class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = (low + high) / 2
        while (low != high):
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid
            else:
                high = mid
        return -1

