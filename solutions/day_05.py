class Solution:
    def getRange(self, arr, target):
        start = 0

        for i, item in enumerate(arr):
            if item == target:
                start = i
                while arr[i] == target:
                    i += 1
                return [start, i - 1]
        return -1

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
assert Solution().getRange(arr, x) == [1, 4]

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 10
print(Solution().getRange(arr, x))
assert Solution().getRange(arr, x) == -1

print('Test pass.')