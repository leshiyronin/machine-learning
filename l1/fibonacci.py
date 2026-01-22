def solution(n: int) -> int:
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n-1):
            k = a
            a = b
            b = k + b
        return b

print(solution(int(input())))
