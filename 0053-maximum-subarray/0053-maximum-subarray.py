#kedans algo
class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum = 0 
        
        for num in nums:
            current_sum = max(num, current_sum + num) 
            max_sum = max(max_sum, current_sum) 
        
        return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 6