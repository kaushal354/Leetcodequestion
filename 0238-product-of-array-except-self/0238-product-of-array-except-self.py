import math

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

nums = [1, 2, 3, 4]
product = Solution()
print(product.productExceptSelf(nums))  # Output: [24, 12, 8, 6]


nums = [1,2,3,4]
Product = Solution()
print(Product.productExceptSelf(nums))