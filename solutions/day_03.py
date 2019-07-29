
class Solution:
    def longestPalindrome(self, string):
        def isPaindrom(string):
            return string == string[::-1]

        substring = []
        for i in range(0, len(string) + 1):
            for j in range(i + 1, len(string) + 1):
                if isPaindrom(string[i:j]) == True:
                    substring.append(string[i:j])
        return max(substring, key=len)

# Fill this in.

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar