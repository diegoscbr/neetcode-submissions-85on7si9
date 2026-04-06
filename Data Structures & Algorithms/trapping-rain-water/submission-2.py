class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L = [0] * n
        R = [0] * n
        res = 0

        # Left pass: max height seen so far from the left
        L[0] = height[0]
        for i in range(1, n):
            L[i] = max(L[i-1], height[i])

        # Right pass: max height seen so far from the right
        R[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            R[i] = max(R[i+1], height[i])

        # Now compute water at each index
        for i in range(n):
            sigma = min(L[i], R[i]) - height[i]
            res += sigma  # sigma is always >= 0 because L and R are maxes

        return res