
def collatz_conjecture(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = 1/2 * n
        else:
            n = 3*n + 1
        result.append(int(n))
    return result

print(collatz_conjecture(10037838738738788737387833733873873377834))