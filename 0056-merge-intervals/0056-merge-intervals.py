class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])  # Sort by start time
        val = [intervals[0]]  # Start with the first interval

        for i in range(1, len(intervals)):
            last = val[-1]
            current = intervals[i]

            if current[0] <= last[1]:  # Overlapping
                last[1] = max(last[1], current[1])  # Merge
            else:
                val.append(current)  # No overlap, just append

        return val


intervals = [[1, 4], [4, 5]]
merge = Solution()
print(merge.merge(intervals))
