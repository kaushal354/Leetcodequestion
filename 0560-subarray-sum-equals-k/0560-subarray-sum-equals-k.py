class Solution(object):
    def subarraySum(self,nums, k):
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}  # To handle subarrays starting from index 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]

            # Update the hashmap
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count


nums = [1, 1, 1]
k = 2
sum1 = Solution()
print(sum1.subarraySum(nums, k))

