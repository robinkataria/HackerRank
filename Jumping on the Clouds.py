def jumpingOnClouds(c,n):
    p=0
    j=0
    
    while p<n-2:
        if c[p+2] == 0 :
            p += 2
            j += 1
        else:
            p += 1
            j += 1
            
    if p == n-2:
        j += 1
    return j

if __name__ == '__main__':
    
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c,n)
    print(str(result) + '\n')
