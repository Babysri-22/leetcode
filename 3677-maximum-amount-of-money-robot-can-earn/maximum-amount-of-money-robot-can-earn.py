
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[j][k] = max coins at column j with k neutralizations used
        dp = [[-float('inf')] * 3 for _ in range(n)]
        
        # Initialize (0,0)
        if coins[0][0] >= 0:
            for k in range(3):
                dp[0][k] = coins[0][0]
        else:
            dp[0][0] = coins[0][0]
            dp[0][1] = 0
            dp[0][2] = 0
        
        # First row
        for j in range(1, n):
            for k in range(3):
                val = coins[0][j]
                
                # Not neutralize
                if dp[j-1][k] != -float('inf'):
                    dp[j][k] = dp[j-1][k] + val
                
                # Neutralize
                if val < 0 and k > 0 and dp[j-1][k-1] != -float('inf'):
                    dp[j][k] = max(dp[j][k], dp[j-1][k-1])
        
        # Remaining rows
        for i in range(1, m):
            new_dp = [[-float('inf')] * 3 for _ in range(n)]
            
            for j in range(n):
                for k in range(3):
                    val = coins[i][j]
                    
                    # From top
                    if dp[j][k] != -float('inf'):
                        # Not neutralize
                        new_dp[j][k] = max(new_dp[j][k], dp[j][k] + val)
                        
                        # Neutralize
                        if val < 0 and k > 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k-1])
                    
                    # From left
                    if j > 0 and new_dp[j-1][k] != -float('inf'):
                        # Not neutralize
                        new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + val)
                        
                        # Neutralize
                        if val < 0 and k > 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k-1])
            
            dp = new_dp
        
        return max(dp[n-1])