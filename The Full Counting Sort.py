def countSort(arr,n):
    for i in range(int(n/2)):
        arr[i][1] = '-'

    newarr = []
    for _ in range(n):
        newarr.append(" ".split())
    
    temp=""
    for i in range(n):
        temp=arr[i][0]
        newarr[int(temp)].append(arr[i][1])
    
    st=""
    for i in newarr:
        for j in i:
            st += str(j) + " "
    print(st.strip())

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())
    
    countSort(arr,n)