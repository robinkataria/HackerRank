def triplets(a, b, c):
    
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))

    x=0
    y=0
    z=0

    count=0
    while y < len(b):
        while x < len(a) and a[x] <= b[y]:
            x += 1
        while z < len(c) and c[z] <= b[y]:
            z += 1
        
        count += x * z
        y += 1
    
    return count

if __name__ == '__main__':

    lenaLenbLenc = input().split()

    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))

    print(triplets(arra, arrb, arrc))
