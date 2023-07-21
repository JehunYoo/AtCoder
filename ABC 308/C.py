# Standings
class Rate:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.x * other.y < self.y * other.x


N = int(input())
A = [0]
B = [0]
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

sort = sorted(range(1, N + 1), key=lambda i: Rate(-A[i], A[i] + B[i]))
print(' '.join(map(str, sort)))