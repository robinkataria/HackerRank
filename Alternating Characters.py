def alternatingCharacters(s):
    
    s += 'x'
    i = 0
    count = 0
    while True:
        if s[i] == 'x':
            break
        elif s[i] == s[i+1]:
            count += 1
            i += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
 
    q = int(input())

    result = []
    for q_itr in range(q):
        s = input()

        result.append(alternatingCharacters(s))

    for ch in result :
        print(str(ch))
