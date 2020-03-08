def flatten(data):
    transform = []
    for i in data:
        if type(i) == list:
            transform += flatten(i)
        else:
            transform.append(i)

    return transform


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))


# 원본: [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# 변환: [1, 2, 3, 4, 5, 6, 7, 8, 9]