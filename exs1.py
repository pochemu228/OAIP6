def quarters(*points):
    count = {
        '1-й': 0,
        '2-й': 0,
        '3-й': 0,
        '4-й': 0
    }
    for x, y in points:
        if x > 0 and y > 0:
            count['1-й'] += 1

        elif x < 0 and y > 0:
            count['2-й'] += 1

        elif x < 0 and y < 0:
            count['3-й'] += 1
            
        elif x > 0 and y < 0:
            count['4-й'] += 1

    return count

data1 = [(1, 1), (-1, 3), (2, -1), (0, 3)]
for k, v in sorted(quarters(*data1).items()):
    print(f'{k}t{v}')

data2 = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
for k, v in sorted(quarters(*data2).items()):
    print(f'{k}t{v}')
