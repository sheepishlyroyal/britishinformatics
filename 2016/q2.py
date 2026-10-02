grid=[]
for i in range(25):
    grid.append(list(map(int, list('0'*25))))


def plane(a,n,b):
    return ((a%n)+b, (a//n)+b)
    # b being offset
    #return (x+b,y+b)


#grid[y][x]
def printgrid():
    global grid
    to_printgrid=[]
    for i in range(25):
        x, y = plane(i,5,4)
        to_printgrid.append(grid[y][x])

    for i in range(5):
        print(*to_printgrid[i*5:i*5+5])

def changegrid(r024):
    x, y = plane(r024, 5, 4)
    grid[y][x] += 1

    if grid[y][x] >= 4:
        grid[y][x] -= 4

        grid[y-1][x] += 1
        grid[y+1][x] += 1
        grid[y][x+1] += 1
        grid[y][x-1] += 1


p, s, n = list(map(int, input().split()))
q=[int(input()) for _ in range(s)]
qsum = p
for i in range(n):
    changegrid(qsum-1)
    qsum += q[i%(len(q))]

printgrid()
