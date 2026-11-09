import math

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
            
        # Calculate minimum possible gap size using the pigeonhole principle
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Initialize buckets with positive/negative infinity to store min and max elements
        buckets_min = [float('inf')] * bucket_count
        buckets_max = [float('-inf')] * bucket_count
        
        # Populate the buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
            
        # Calculate the maximum gap between adjacent non-empty buckets
        max_gap = 0
        previous_max = min_val
        
        for i in range(bucket_count):
            # Skip empty buckets
            if buckets_min[i] == float('inf'):
                continue
                
            # Gap is the difference between current bucket's min and previous bucket's max
            max_gap = max(max_gap, buckets_min[i] - previous_max)
            previous_max = buckets_max[i]
            
        return max_gap
