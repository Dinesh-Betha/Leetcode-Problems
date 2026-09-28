class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        count = 0
        newheights = sorted(heights)
        for i in range(n):
            if heights[i] != newheights[i]:
                count += 1
        return count