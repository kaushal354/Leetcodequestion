class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers.sort()
        left = 0
        right = len(numbers)-1
        while(left < right):
            if (numbers[left] + numbers[right]) == target:
                return [left+1, right+1]
            if (numbers[left]+numbers[right]) > target:
                right -=1
            else:
                left +=1
        return []

        