class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        for x in nums1:
            freq[x] = freq.get(x,0) + 1
        ans = []
        for x in nums2:
            if x in freq and freq[x] > 0:
                ans.append(x)
                freq[x] -= 1
        return ans
        