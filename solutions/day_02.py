
class Solution:
    def lengthOfLongestSubstring(self, string):
    # Fill this in.
        start = 0
        max_len = 0
        char_set = {}
        char_set[string[0]] = 0

        for i, character in enumerate(string[1::]):
            if character not in char_set:
                char_set[character] = i
            else:
                if char_set[character] >= start:
                    currlen = i - start
                    if max_len < currlen:
                        max_len = currlen
                    start = char_set[string[i]] + 1

                char_set[character] = i
        if max_len < i - start:
            max_len = i - start

        return max_len

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10