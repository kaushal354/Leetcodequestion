class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


nums = [1, 2, 3, 4]
p = Solution()
print(p.productExceptSelf(nums))
