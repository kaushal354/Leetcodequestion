class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lo = 0
        mid = 0
        hi = len(nums)-1
        while (mid <= hi):
            if nums[mid] ==0:
                nums[lo] , nums[mid] = nums[mid],nums[lo]
                lo +=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid],nums[hi] = nums[hi] , nums[mid]
                hi -=1
        return nums
        