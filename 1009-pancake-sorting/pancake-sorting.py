class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans = []
        for k in range(n,0,-1):
            i = arr.index(k)
            if i == k - 1:
                continue
            if i != 0:
                arr[:i + 1] = arr[:i + 1][::-1]
                ans.append(i + 1)
            arr[:k] = arr[:k][::-1]
            ans.append(k)
        return ans
        