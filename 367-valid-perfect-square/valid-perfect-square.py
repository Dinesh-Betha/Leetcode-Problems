class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            product = (mid*mid)
            if product == num:
                return True
            elif product < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
        