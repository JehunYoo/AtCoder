M = int(input())
D = list(map(int, input().split()))

month = 1
day = (sum(D) + 1) // 2

while day > 0:
    if day > D[month - 1]:
        day -= D[month - 1]
    else:
        break
    month += 1

print(month, day)