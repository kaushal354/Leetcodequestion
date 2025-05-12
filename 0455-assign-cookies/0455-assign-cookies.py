class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l=0
        g.sort()
        s.sort()
        for cSize in s:
            if cSize >= g[l]:
                l+=1
                if l == len(g):
                    break
        return l


g = [1,2,3]
s = [1,1]
assign = Solution()
print(assign.findContentChildren(g,s))

        