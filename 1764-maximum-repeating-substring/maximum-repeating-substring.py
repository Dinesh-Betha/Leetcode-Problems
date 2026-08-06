class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_count = 0
        count = 0
        while word * (count + 1) in sequence:
            count += 1
        return count
        