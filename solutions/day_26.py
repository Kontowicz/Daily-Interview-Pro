def courses_to_take(course_to_prereqs):
    to_return = []

    for key, value in course_to_prereqs.items():
        if to_return == []:
            for v in value:
                to_return.append(v)
            to_return.append(key)
        else:
            pos = to_return.index(key)
            if pos == -1:
                return None
            for item in value:
                to_return.insert(pos, item)

    return list(set(to_return))

courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}
assert courses_to_take(courses) == ['CSC100', 'CSC200', 'CSC300']
print('Test pass.')