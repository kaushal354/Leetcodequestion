from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        nums3 =  max(freq, key = freq.get)
        return nums3


         
        