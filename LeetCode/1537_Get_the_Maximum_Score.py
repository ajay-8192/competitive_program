class Solution:
    def maxSum(self, A, B):
        i, j, n, m = 0, 0, len(A), len(B)
        a, b, mod = 0, 0, 10**9 + 7
        while i < n or j < m:
            if i < n and (j == m or A[i] < B[j]):
                a += A[i]
                i += 1
            elif j < m and (i == n or A[i] > B[j]):
                b += B[j]
                j += 1
            else:
                a = b = max(a, b) + A[i]
                i += 1
                j += 1
        return max(a, b) % mod
