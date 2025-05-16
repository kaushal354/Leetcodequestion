class Solution(object):
    def subarraySum(self, nums, k):
        from collections import defaultdict
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sum_count:
                count += prefix_sum_count[curr_sum - k]
            prefix_sum_count[curr_sum] += 1
            
        return count

nums = [1, 1, 1]
k = 2
sum1 = Solution()
print(sum1.subarraySum(nums, k))

