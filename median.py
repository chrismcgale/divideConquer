
#arr will always have at most 5 elements and at least 3
def qMed(arr):
    r = len(arr) //2
    arr.sort(key = int)
    return arr[r]



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
    if len(arr) < 5:
        meds.append(int(qMed(arr)))
    return median(meds)



if __name__ == '__main__':
    myArr = [(int)]
    file = open("test.txt", "r")
    line = file.readline()
    myArr = line.split()
    file.close()
    print(median(myArr))