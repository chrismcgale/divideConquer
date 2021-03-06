#arr will always have at most 5 elements and at least 3
def qMed(arr):
    r = len(arr) // 2
    arr.sort(key = int)
    return arr[r]

# Runtime is O(n)
def median(arr):
    if len(arr) == 0:
        return "N/A"
    if len(arr) == 1:
        return arr[0]
        
    i = 0
    d = 5
    meds = []

    while d <= len(arr):
        meds.append(int(qMed(arr[i:d])))
        i += 5
        d += 5

    # Incase list isn't multiple of 5
    if d != len(arr):
        meds.append(int(qMed(arr[i: i + len(arr) - d + 5])))

    return median(meds)



if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    print(median(a))
