
def buddyStrings(A, B):
    if A == B:
        return True

    if len(A) != len(B):
        return False

    A_dict = {}
    B_dict = {}

    for i in range(0, len(A)):
        if A[i] not in A_dict:
            A_dict[A[i]] = 1
        else:
            A_dict[A[i]] = A_dict[A[i]] + 1

        if B[i] not in B_dict:
            B_dict[B[i]] = 1
        else:
            B_dict[B[i]] = B_dict[B[i]] + 1

    for key, value in A_dict.items():
        if key not in B_dict:
            return False

    for key, value in B_dict.items():
        if key not in A_dict:
            return False

    counter = 0

    for key in A_dict:
        counter += abs(A_dict[key] - B_dict[key])

    return counter <= 1

assert buddyStrings('aaaaaaabc', 'aaaaaaacb') == True
# True
assert buddyStrings('aaaaaabbc', 'aaaaaaacb') == False
False