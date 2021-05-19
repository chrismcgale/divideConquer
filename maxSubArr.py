

def maxSubArr(arr):
    if len(arr) == 1 :
        return arr[0]
    else:
        m = len(arr)//2
        l = maxSubArr([:m])
        r = maxSubArr(arr[m:])
        




if __name__ == '__main__':
    myArr = [(int)]
    file = open("test.txt", "r")
    line = file.readline()
    myArr = line.split()
    file.close()
    print(countInversions(myArr))