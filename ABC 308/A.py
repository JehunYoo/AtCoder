# New Scheme
S = list(map(int, input().split()))

answer = True
prev = S[0]
for s in S[1:]:
    if not (prev <= s):
        answer = False
        break
    prev = s
if answer:
    for s in S:
        if (not (100 <= s <= 675)) or s % 25 != 0:
            answer = False
            break

if answer:
    print("Yes")
else:
    print("No")