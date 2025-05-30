from collections import Counter
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        num = []
        result = []
        for num1 in grid:
            for i in num1:
                num.append(i)
        freq = Counter(num)
        max_dict = max(freq,key = freq.get)
        result.append(max_dict)
        n = len(num)+1
        for i in range(1,n+1):
            if i not in freq:
                result.append(i)
                return result
         




            


            
                

        