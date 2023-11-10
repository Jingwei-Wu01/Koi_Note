n = int(input('enter a number:'))
pef_num = 0
for i in range(n):   
    while True:
        pef_num += 1
        yinzi = []
        sum = 0
        for j in range(1, pef_num):
            if pef_num % j == 0:
                yinzi.append(j)
                sum += j
        if sum == pef_num:
            break

print(f"The {n} perfect number is: {pef_num}")