def mergeCount(l, r):
    i = j = k = 0
    ret = 0
    while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                i += 1
            else:
                j += 1
                ret += len(l) - i
            k += 1
    return ret


#Counts the number of key pairs i < j such that arr[i] > arr[j]
#Runs in O(nlogn) as in merge sort
def countInversions(arr):
    if len(arr) == 1 :
        return 0
    else:
        m = len(arr)//2
        s1 = countInversions(arr[:m])
        s2 = countInversions(arr[m:])
        s3 = mergeCount(arr[:m], arr[m:])
        return s1 + s2 + s3



if __name__ == '__main__':
    myArr = [(int)]
    file = open("test.txt", "r")
    line = file.readline()
    myArr = line.split()
    file.close()
    print(countInversions(myArr))