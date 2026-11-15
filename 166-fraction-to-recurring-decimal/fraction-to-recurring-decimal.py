class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator edge case
        if numerator == 0:
            return "0"
        
        res = []
        
        # Determine the sign using XOR
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
            
        # Work with positive values to simplify division
        num, den = abs(numerator), abs(denominator)
        
        # Append the integer part
        quotient, remainder = divmod(num, den)
        res.append(str(quotient))
        
        # If there is no remainder, return the whole number
        if remainder == 0:
            return "".join(res)
            
        res.append(".")
        
        # Map each remainder to its index in the result list
        remainder_map = {}
        
        while remainder != 0:
            # If the remainder was seen before, a cycle is detected
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                res.insert(idx, "(")
                res.append(")")
                break
                
            # Record the index where this remainder's digit will be placed
            remainder_map[remainder] = len(res)
            
            # Perform the next step of long division
            remainder *= 10
            digit, remainder = divmod(remainder, den)
            res.append(str(digit))
            
        return "".join(res)
