def hourglassSum(arr):
    add = []
    for i in range(4):
        for j in range(4):
            add.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    m = max(add)
    return m

if __name__ == '__main__':
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglassSum(arr)

print(str(result) + '\n')
