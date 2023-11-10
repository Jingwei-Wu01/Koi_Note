lst = [3, 4, 3, 1, 2, 3, 100, -4]
lst.sort()

num = []
count = []

for i in range(len(lst)):
    if lst[i] not in num:
        num.append(lst[i])
        count.append(1)
    else:
        count[num.index(lst[i])] += 1

for i in range(len(num)):
    print(f'{num[i]}: {count[i]}')


# lst = [3, 4, 3, 1, 2, 3, 100, -4]

# lst.sort()
# num = []
# count = []
# num.append(lst[0])
# count.append(1)
# for i in range(1, len(lst)):
#     if lst[i] == lst[i - 1]:
#         count[-1] += 1
#     else:
#         num.append(lst[i])
#         count.append(1)