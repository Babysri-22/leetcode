class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        nums = [ord(c) - ord('A') for c in word]
        n = len(nums)
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == n:
                return 0
            
            cur = nums[i]
            
            # Option 1: use finger 1
            use_f1 = dist(f1, cur) + dp(i + 1, cur, f2)
            
            # Option 2: use finger 2
            use_f2 = dist(f2, cur) + dp(i + 1, f1, cur)
            
            return min(use_f1, use_f2)
        
        return dp(0, -1, -1)