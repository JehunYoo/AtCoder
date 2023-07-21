# Default Price
N, M = map(int, input().split())
colors = input().split()
dcolors = input().split()
prices = list(map(int, input().split()))

menu = {d: p for d, p in zip(dcolors, prices[1:])}
pay = 0
for color in colors:
    if color in menu:
        pay += menu[color]
    else:
        pay += prices[0]

print(pay)