def maximumToys(prices, k):
    prices.sort()
    count=0
    for amt in prices:
        if amt<k:
            count+=1
            k=k-amt
    return count
    
if __name__ == '__main__':

    nk = input().split()
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    print(maximumToys(prices, k))
