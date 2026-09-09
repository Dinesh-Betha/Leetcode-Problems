class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        freq = {0:1}
        count = 0
        for i in nums:
            prefixSum += i

            if prefixSum - k in freq:
                count += freq[prefixSum-k]
            
            freq[prefixSum] = freq.get(prefixSum, 0) + 1
        return count