# 袋子里有N个球，每次只能拿1个或者2个或者3个，请输出所有可能的拿法
#


def digui(n):

    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1], [2]]
    elif n == 3:
        return [[1, 1, 1], [1, 2], [2, 1], [3]]

    result = []
    for i in digui(n - 1):
        result.append(i + [1])
    for i in digui(n - 2):
        result.append(i + [2])
    for i in digui(n - 3):
        result.append(i + [3])

    return result

n = 4
print(digui(n))