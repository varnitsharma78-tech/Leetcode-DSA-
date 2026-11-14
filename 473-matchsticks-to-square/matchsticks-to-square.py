from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        
        # A square requires 4 equal sides
        if total_length % 4 != 0:
            return False
            
        target_side = total_length // 4
        
        # Sort descending so larger matchsticks fail fast if invalid
        matchsticks.sort(reverse=True)
        
        # If the longest stick exceeds the target side length, it is impossible
        if matchsticks[0] > target_side:
            return False
            
        sides = [0] * 4
        
        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return True
                
            for i in range(4):
                # Skip if adding this stick exceeds the target side length
                if sides[i] + matchsticks[index] > target_side:
                    continue
                    
                # Skip duplicate side states to avoid redundant work
                if i > 0 and sides[i] == sides[i - 1]:
                    continue
                    
                sides[i] += matchsticks[index]
                if backtrack(index + 1):
                    return True
                sides[i] -= matchsticks[index]
                
            return False
            
        return backtrack(0)
