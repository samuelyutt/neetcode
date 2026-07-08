class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Return the maximum length of a substring that can be made all one char with up to k replacements."""
        counts = [0] * 26
        left = 0
        max_count = 0
        best = 0

        for right, ch in enumerate(s):
            index = ord(ch) - ord("A")
            counts[index] += 1
            max_count = max(max_count, counts[index])

            # If we need more than k replacements, shrink the window.
            while (right - left + 1) - max_count > k:
                counts[ord(s[left]) - ord("A")] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best

