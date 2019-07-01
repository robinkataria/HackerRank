n = int(input())
inp = input()
l = inp.split()
s = set(l)
s = list(s)
s.sort()

def zerolistmaker(s):
    count = [0] * s
    return count

def sockMerchant(n, l):
    count = zerolistmaker(len(s))
    for i in range(0, len(s)):
        for j in range(0, n):
            if s[i] == l[j]:
                count[i] += 1
        count[i] = int(count[i] / 2)

    t = 0
    for i in range(0, len(s)):
        t = t + count[i]
    return t

print((sockMerchant(n, l)))
