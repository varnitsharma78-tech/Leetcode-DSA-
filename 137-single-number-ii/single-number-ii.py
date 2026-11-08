class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update 'ones' only if the bit is not already in 'twos'
            ones = (ones ^ num) & ~twos
            # Update 'twos' only if the bit is not already in 'ones'
            twos = (twos ^ num) & ~ones
            
        return ones
