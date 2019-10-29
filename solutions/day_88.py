def topKFrequent(words, k):
    dict = {}
    for item in words:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1

    dictlist = []
    for key, value in dict.items():
        temp = [key, value]
        dictlist.append(temp)

    dictlist.sort(key=lambda x:x[1], reverse= True)

    return [x[0] for i, x in enumerate(dictlist) if i < k]

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2

assert topKFrequent(words, k) == ['pro', 'daily']
print(topKFrequent(words, k))
print('Test pass.')