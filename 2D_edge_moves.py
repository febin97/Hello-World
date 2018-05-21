pos_ls=[]
noblock_ls = []
blocks_ls = []
set_block_pos = []
L_b_diagonal = -1
R_b_diagonal = -1
L_t_diagonal = -1
R_t_diagonal = -1
L_r_diagonal = -1
R_r_diagonal = -1
T_c_diagonal = -1
B_c_diagonal = -1
def findPos(A,character):
    for i in range(5):
        for j in range(5):
            if A[i][j] == character:
                return i,j
            
def isNeighbour(x1,y1,x2,y2):
    if x1 != x2 and y1 != y2:
        if abs(x1-x2)+abs(y1-y2) <= 2:
            return True         
    else:
        if abs(x1-x2)+abs(y1-y2) < 2:
            return True
    return False
def pathMoves(M1,A1,pos1,ls):
    L_b_diagonal = -1
    R_b_diagonal = -1
    L_t_diagonal = -1
    R_t_diagonal = -1
    L_row = -1
    R_row = -1
    T_column = -1
    B_column = -1
    x1,y1 = findPos(A1,pos1)
    c= M1[x1][y1]
    for j in range(len(ls)):
        x2,y2 = findPos(A1,ls[j])
        if x1 == x2 or y1 == y2:
            if x1 == x2 and y1>y2 and L_row == -1:
                c = c-1
                L_row = 1
            elif x1 == x2 and y1 < y2 and R_row == -1:
                c=c-1
                R_row = 1
            elif y1 == y2 and x1>x2 and T_column == -1:
                c=c-1
                T_column = 1
            elif y1 == y2 and x1<x2 and B_column == -1:
                c=c-1
                B_column = 1
        elif abs(x1-x2) == abs(y1-y2):
            if x2>x1 and y2>y1 and R_t_diagonal==-1:
                c=c-1
                R_t_diagonal = 1
            elif x2>x1 and y2<y1 and L_t_diagonal==-1:
                c=c-1
                R_b_diagonal = 1
            elif x2<x1 and y2>y1 and R_b_diagonal==-1:
                c=c-1
                R_b_diagonal = 1
            elif x2<x1 and y2<y1 and L_b_diagonal==-1:
                c=c-1
                L_b_diagonal = 1
    return c   
    
def findNoOfMoves(M1,A1,pos1,ls):
    x1,y1 = findPos(A1,pos1)
    c= M1[x1][y1]
    for j in range(len(ls)):
        x2,y2 = findPos(A1,ls[j])
        if isNeighbour(x1,y1,x2,y2):
            c=c-1
    return c

M = [[0 for x in range(5)] for y in range(5)]
A = [[0 for x in range(5)] for y in range(5)]
ch = 'A'
for i in range(5):
     for j in range(5):
         if i in [0,4] and j in [0,4]:
             M[i][j] = 3
         elif ( j in [0,4] and i in [1,2,3]) or (i in [0,4] and j in [1,2,3]):
             M[i][j] = 5
         else:
             M[i][j] = 8
for i in range(5):
     for j in range(5):
         A[i][j] = ch
         ch = chr(ord(ch)+1)
for i in range(5):
     for j in range(5):
        print(A[i][j],end=" ")
     print()
pos_ls = input("Enter the initial positions\n").split(",")
noblock_ls = [int(n) for n in input("Enter the no of blocking postions of each initial postion in order\n").split(",")]
for i in range(len(pos_ls)):
    block_ls= []
    print("Enter the blocking  positions of ",pos_ls[i])
    block_ls = input().split(",")
    for j in range(len(block_ls)):
        if set_block_pos.count(block_ls[j]) < 1:
            set_block_pos.append(block_ls[j])
    print(set_block_pos)
    c = findNoOfMoves(M,A,pos_ls[i],set_block_pos)
    print("Possible No of Moves =  ",c)
    c= pathMoves(M,A,pos_ls[i],set_block_pos)
    print("Possible No of Edge Moves =  ",c)
