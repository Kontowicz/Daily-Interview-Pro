def merge(intervals):
    intervals.sort(key=lambda x : x[0])

    to_return = []
    to_return.append(intervals[0])
    for i in range(1, len(intervals)):
        top = to_return[-1]

        if top[1] < intervals[i][0]:
            to_return.append(intervals[i])

        elif top[1] < intervals[i][1]:
            top[1] = intervals[i][1]
            to_return.pop()
            to_return.append(top)

    return to_return


assert merge([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
print('Test pass.')