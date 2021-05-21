# Kuratsuba's Algorithm
# x = x1 * 2^(n/2) + x0
# y = y1 * 2^(n/2) + y0
# xy = (x1 * 2^(n/2) + x0)(y1 * 2^(n/2) + y0)
#   = x1y1 * 2^n + (x1y0 + x0y1) * 2^(n/2) + x0y0
#   = x1y1 * 2^n + 9(x1 + x0)(y1 + y0) - x1y1 - x0y0) * 2^(n/2) + x0y0
# Runtime is O(n^1.59)
def recurMult(x, y):
    n = len(str(x))
    n2 = n // 2

    if n == 1:
        return x * y

    x1 = int(str(x)[:n2])
    x0 = int(str(x)[n2:])
    y1 = int(str(y)[:n2])
    y0 = int(str(y)[n2:])

    # Recursive steps
    x1y1 = recurMult(x1, y1)
    x0y0 = recurMult(x0, y0)
    p = (recurMult(x1 + x0, y1 + y0) - x1y1 - x0y0) * (2 ** n2)

    return x1y1 * (2 ** n) + p + x0y0

# Generic main
if __name__ == '__main__':
    myArr = [(int)]
    file = open("test.txt", "r")
    line1 = file.readline()
    x = int(line1)
    line2 = file.readline()
    y = int(line2)
    file.close()
    #splice to remove 1b from binary
    print(bin(recurMult(x, y))[2:])
    
