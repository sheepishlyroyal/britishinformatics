def split(s,letter):
    global N
    #'LRLL'
    s=s[::-1]


    try:
        loc=s.index(letter)

        q=s[loc+1:]
        return q[::-1], False
    
    except: 
        return None, True

prom=input()

def P(s) -> (int, int):
    
    ls=split(s, 'L')
    rs=split(s,'R')

    if ls[1]:
        ls = (1,0) 
    else:
        if ls[0] == '':
            ls = (1,1) 
        else:
            ls = P(ls[0]) 


    
    if rs[1]:
        rs = (0,1) 
    else:
        if rs[0] == '':
            rs = (1,1) 
        else:
            rs = P(rs[0])

    print((ls, rs))
    return (ls[0]+rs[0]), (ls[1]+rs[1])

print(P(prom))
