from math import sqrt,floor,ceil

def encryption(s):
    l = len(s)
    
    row = floor(sqrt(l))
    column = ceil(sqrt(l))
    
    if row * column < l:
        row = column
    
    grid = []
    for i in range(row):
        grid.append( ["" for i in range(column)] )
    
    k=0
    for i in range(row):
        for j in range(column):
            if k>=l:
                break
            else:
                grid[i][j]=s[k]
                k+=1
    news = []
    for i in range(column):
        news.append( ["" for i in range(row)] )
    
    for i in range(column):
        for j in range(row):
            news[i][j] = grid[j][i]
    
    nstring = ""    
    for i in news:
        for j in i:
            nstring += str(j)
        nstring += " "
   
    return nstring                    

if __name__ == '__main__':
    
    s = input().replace(" ","")
    print( encryption(s) )
