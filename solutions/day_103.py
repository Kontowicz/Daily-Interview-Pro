
def find(part, start, end):
    if end >= start:
        piv = (start + end) // 2

    if piv == part[piv]:
        return piv
    if piv > part[piv]:
        return find(part, piv + 1, end)
    else:
        return find(part, start, piv - 1)

    return

def find_fixed_point(nums):
    return find(nums, 0, len(nums))

assert find_fixed_point([-5, 1, 3, 4]) == 1
print(find_fixed_point([-5, 1, 3, 4]))
print('Test pass.')