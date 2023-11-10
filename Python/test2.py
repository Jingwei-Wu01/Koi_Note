# 判断一个数组内的数是不是单峰数列
# 单峰数列：前面的数递增，后面的数递减

def isSinglePeak(arr):
    if len(arr) < 3:
        return False
    # 判断是否是单峰数列
    # 找到最大值的下标
    maxIndex = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    # 判断最大值的下标是否是第一个或者最后一个
    if maxIndex == 0 or maxIndex == len(arr) - 1:
        return False
    # 判断前面的数是否递增
    for i in range(1, maxIndex):
        if arr[i] <= arr[i - 1]:
            return False
    # 判断后面的数是否递减
    for i in range(maxIndex + 1, len(arr)):
        if arr[i] >= arr[i - 1]:
            return False
    return True