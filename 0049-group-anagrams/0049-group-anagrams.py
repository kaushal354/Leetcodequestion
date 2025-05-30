from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
p = Solution()
print(p.groupAnagrams(strs))