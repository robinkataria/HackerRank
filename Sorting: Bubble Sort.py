def countSwaps(a,n):
    swap=0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap+=1
    
    print(f"Array is sorted in {swap} swaps.")
    print("First Element:" , a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a,n)
