def permute(nums):
    to_return = []
    def get_parm(arr, left, right):
        if left==right:
            tmp = []
            for item in arr:
                tmp.append(item)
            to_return.append(tmp)
        else:
            for i in range(left, right+1):
                arr[left], arr[i] = arr[i], arr[left]
                get_parm(arr, left+1, right)
                arr[left], arr[i] = arr[i], arr[left]
    get_parm(nums,0, len(nums)-1)
    return to_return

print(permute([1, 2, 3]))