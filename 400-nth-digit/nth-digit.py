class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_size = 1
        count = 9
        start_num = 1
        
        # Step 1: Find the length category (1-digit, 2-digit, etc.) where the nth digit lies
        while n > digit_size * count:
            n -= digit_size * count
            digit_size += 1
            count *= 10
            start_num *= 10
            
        # Step 2: Find the exact target number containing the nth digit
        target_num = start_num + (n - 1) // digit_size
        
        # Step 3: Extract the specific digit from that number
        digit_index = (n - 1) % digit_size
        return int(str(target_num)[digit_index])
