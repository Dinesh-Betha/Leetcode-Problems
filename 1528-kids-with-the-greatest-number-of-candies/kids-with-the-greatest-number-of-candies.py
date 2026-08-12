class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        
        result = []
        for i in candies:
            if i + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
                
        return result

