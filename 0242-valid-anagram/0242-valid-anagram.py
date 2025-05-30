
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq1 = sorted(s)
        freq2 = sorted(t)
        if len(freq1) != len(freq2):
            return False
        else:
            for i in range(len(freq1)):
                if freq1[i] != freq2[i]:
                    return False
        return True

nums = "anagram"
nums1 = "nagaram"
p = Solution()
print(p.isAnagram(nums,nums1))