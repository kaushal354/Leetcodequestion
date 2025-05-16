from collections import Counter


class Solution(object):
    def findDuplicate(self, nums):
        freq = Counter(nums)
        maxnum = max(freq,key = freq.get)
        return maxnum
        