class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def count(arr):
            ans = 0
            for i in range(n-1, -1, -1):
                if arr[i] == 0:
                    ans += 1
                else:
                    break
            return ans
            
        arr = [count(row) for row in grid]
        ans = 0
        for i in range(n):
            target = n - i - 1
            if arr[i] >= target:
                continue
            flag = False
            for j in range(i+1, n):
                if arr[j] >= target:
                    flag = True
                    ans += (j - i)
                    arr[i+1:j+1] = arr[i:j]
                    break
            if not flag:
                return -1
        
        return ans
