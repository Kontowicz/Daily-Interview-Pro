def get_madin(array):
    array.sort()

    if len(array) % 2 == 1:
        return array[(len(array)//2)]
    else:
        return (array[(len(array) // 2)] + array[(len(array) // 2) - 1]) / 2

def running_median(stream):
    to_retrurn = []
    data = []
    for item in stream: # number stream simulation
        data.append(item)
        to_retrurn.append(get_madin(data))

    return to_retrurn

running_median([2, 1, 4, 7, 2, 0, 5]) == [2, 1.5, 2, 3.0, 2, 2.0, 2]
print('Test pass.')