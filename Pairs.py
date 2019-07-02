def pairs(k, arr):
    
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[i] + k)
    
    common = set(arr) & set(newarr)
    return len(common)

if __name__ == '__main__':
   
    nk = input().split()
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))

    print(pairs(k, arr))
