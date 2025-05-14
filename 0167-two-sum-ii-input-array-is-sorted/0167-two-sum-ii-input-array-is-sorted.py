class Solution:
    def twoSum(self, numbers, target):
        a = 0
        b = len(numbers) - 1
        while a < b:
            element = numbers[a] + numbers[b]
            if element == target:
                return [a + 1, b + 1]

            elif element < target:
                a += 1
            else:
                b -= 1

        