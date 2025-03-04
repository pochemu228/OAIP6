def quarters(*points):
    quarter_count = {
        'I': 0,
        'II': 0,
        'III': 0,
        'IV': 0
    }

    for x, y in points:
        if x > 0 and y > 0:
            quarter_count['I'] += 1

        elif x < 0 and y > 0:
            quarter_count['II'] += 1

        elif x < 0 and y < 0:
            quarter_count['III'] += 1

        elif x > 0 and y < 0:
            quarter_count['IV'] += 1
        else:
            pass

    return quarter_count


data = [(1, 1), (-1, 2), (-3, -1)]
for k, v in sorted(quarters(*data).items()):
    print(f'{k}:\t{v}')

data = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
for k, v in sorted(quarters(*data).items()):
    print(f"{k}:\t{v}")
