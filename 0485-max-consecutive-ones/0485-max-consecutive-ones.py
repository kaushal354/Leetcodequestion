class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxcon = 0
        for num in nums:
            if num == 1:
                count+=1
            else:
                maxcon = max(maxcon, count)
                count = 0
         
        return max(maxcon, count)

                
        