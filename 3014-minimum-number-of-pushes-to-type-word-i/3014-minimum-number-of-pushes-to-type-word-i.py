class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0

        for i in range(len(word)):
            total += (i // 8) + 1

        return total