from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        freq = Counter(nums)
        for i,j in freq.items():
            if j > len(nums)/3:
                ans.append(i)
        return ans


        
        