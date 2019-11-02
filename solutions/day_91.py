def compareVersion(version1, version2):
    ver_1 = version1.split('.')
    ver_2 = version2.split('.')

    if len(ver_1) > len(ver_2):
        return 1
    elif len(ver_1) < len(ver_2) :
        return -1

    for i in range(0, len(ver_1)):
        if int(ver_1[i]) > int(ver_2[i]):
            return 1
        else:
            return -1

    return None

version1 = "1.0.1"
version2 = "1"
assert compareVersion(version1, version2) == 1
print(compareVersion(version1, version2))
print('Test pass.')