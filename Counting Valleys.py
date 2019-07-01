n = int(input())
s = input()

def countingValleys(n, s):
    count = 0
    v = 0

    for i in s:
        if i == 'U':
            count += 1
            if count == 0:
                v += 1

        else:
            count -= 1

    return v

print(countingValleys(n, s))
