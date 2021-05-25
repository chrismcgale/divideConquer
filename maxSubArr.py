import numpy as np
# O(n)
def maxEnd(l):
    n = len(l)
    arr = []
    i = 1
    curr = l[n - i]
    real = 0
    while i <= n:
        if l[n - i] + real > curr:
            arr = l[n - i:n]
            curr = real
        real += l[n - i]
        i += 1
    return arr

# O(n)
def maxBegin(r):
    n = len(r)
    arr = []
    i = 0
    curr = r[0]
    real = 0
    while i < n:
        if r[i] + real > curr:
            arr = r[0:i]
            curr = real
        real += r[i]
        i += 1
    return arr 



# Runtime: O(n)
def maxSubArr(arr):
    if len(arr) == 1 :
        return [arr[0]]
    else:

        m = len(arr) // 2
        # Recursive step
        l = maxSubArr(arr[:m])
        r = maxSubArr(arr[m:])

        # Note: if true max is cross of l and r [i, j] it must be true that both
        # [i, n/2] is a max array ending with n2 and [n/2, j] is a max array 
        # starting with n/2
        lMid = maxEnd(arr[:m])
        rMid = maxBegin(arr[m:])

        sl = sum(l) # O(n)
        sr = sum(r) # O(n)
        sm = sum(lMid) + sum(rMid) # O(n)

        if sl >= sr and sl >= sm:
            return l
        elif sr >= sl and sr >= sm:
            return r
        else:
             return lMid + rMid
        

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    print(maxSubArr(a))