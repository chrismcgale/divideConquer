import math
# Kuratsuba's Algorithm
# x = x1 * 2^(n/2) + x0
# y = y1 * 2^(n/2) + y0
# xy = (x1 * 2^(n/2) + x0)(y1 * 2^(n/2) + y0)
#   = x1y1 * 2^n + (x1y0 + x0y1) * 2^(n/2) + x0y0
#   = x1y1 * 2^n + (x1 + x0)(y1 + y0) - x1y1 - x0y0) * 2^(n/2) + x0y0
# Runtime is O(n^1.59)
def recurMult(x, y):
    n = min(len(x), len(y))
    n2 = n // 2

    print(x, y)

    if n == 1:
        return str(bin(int(x, 2) * int(y, 2))[2:])

    x1 = x[:n2]
    x0 = x[n2:]
    y1 = y[:n2]
    y0 = y[n2:]

    # Recursive steps
    x1y1 = int(recurMult(x1, y1), 2)
    x0y0 = int(recurMult(x0, y0), 2)
    p = int(recurMult(str(bin(int(x1, 2) + int(x0, 2)))[2:], str(bin(int(y1, 2) + int(y0, 2)))[2:]), 2) - x1y1 - x0y0

    if n % 2 == 1:
        n += 1
        n2 += 1
        
    return str(bin(x1y1 * (2 ** n) + p * (2 ** n2) + x0y0))[2:]

# Generic main
if __name__ == '__main__':
    myArr = []
    file = open("test.txt", "r")
    line1 = file.readline()
    x = line1.rstrip("\n")
    line2 = file.readline()
    y = line2.rstrip("\n")
    file.close()

    print(recurMult(x, y))
    
