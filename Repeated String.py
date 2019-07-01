s = input()
n = int(input())

def repeatedString(l, n):
    count = 0
    for ch in l:
        if ch=='a':
            count+=1

    d = int(n / len(l))
    count = count * d
    m = int(n % len(l))
    for i in range(0,m):
        if l[i]=='a':
            count += 1
    
    return count

print(repeatedString(s, n))
