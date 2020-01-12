def meeting_rooms(meetings):
    eventList = []

    for (start, end) in meetings:
        eventList.append((start, 'start'))
        eventList.append((end, 'end'))

    eventList.sort()

    required = 0
    toReteurn = 0

    for (time, event) in eventList:
        if event == 'start':
            required += 1
        elif event == 'end':
            required -= 1
        if required > toReteurn:
            toReteurn = required
    return toReteurn

assert meeting_rooms([(0, 10), (10, 20)]) == 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1
assert meeting_rooms([(20, 30), (10, 21), (0, 50)]) == 3
print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)

print('Test pass.')