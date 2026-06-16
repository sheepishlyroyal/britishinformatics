board=[]
for i in range(3): board.append(list('.'*11))
for i in range(5):
    screen5 = input()
    screen = '.'*3+screen5+'.'*3
    board.append(list(screen))
for i in range(3): board.append(list('.'*11))

boardsave=board
board=boardsave
print(board)
n=0


def generate(n, hashtag):
    global boardsave, board
    surround = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    if hashtag == True:
        gameboard = boardsave
    else:
        gameboard = board
    for l in range(n):
        for y in range(len(gameboard)):
            for x in range(len(gameboard[y])):
                if gameboard[y][x] == '0':
                    count=0
                    for q in range(8):
                        
                        if 0 <= x+surround[q][0] < 11 and 0 <= y+surround[q][1] < 11:
                            if gameboard[(y+surround[q][1])][(x+surround[q][0])] == '0':
                                count+=1
                        if not 2 <= count <= 3:
                            gameboard[y][x] = '.'
                else:
                    count=0
                    for q in range(8):
                        
                        if 0 <= x+surround[q][0] < 11 and 0 <= y+surround[q][1] < 11:
                            if gameboard[(y+surround[q][1])][(x+surround[q][0])] == '0':
                                count+=1
                        if count == 3:
                            gameboard[y][x] = '0'

                    

    board = gameboard
    return ("".join(board))
                
p=list(input())
while p != '-1':
    if '#' in p: 
        n=int(p.remove('#'))

        print(generate(n, True))


    elif '+' in p: 
        n+= int(p.remove('+'))
        print(generate(n,False))
    p=list(input())
print('exiting...')

