def new_board():
    board = {}
    return board

def is_free(board,x,y):
    return (x,y) not in board 

def place_piece(board,x,y,player):
    if is_free(board,x,y) == True:
        board[(x,y)] = player
        print(player + ' now occipies position x=' + str(x) + ' y=' + str(y))
        return True
    else:
        print("Position occupied")
        return False

def get_piece(board,x,y):
    if is_free(board,x,y) == True:
        return False
    else:
        return board[(x,y)]
         

def remove_piece(board,x,y):
    if is_free(board,x,y) == True:
        return False
    else:
        del board[(x,y)]
        print('Piece succesfully removed')
        return True

def move_piece(board,x,y,a,b):
    if is_free(board,x,y) or is_free(board,a,b) == False:
        return False
    else:
        print (board[(x,y)] + ' succesfully moved to x=' + str(a) + ' y=' + str(b))
        board[(a,b)] = board[(x,y)]
        del board[(x,y)]
        return True


def count(board,axis,value,player):
    count = 0
    if axis == "column":
        for i in board:
            if i[0] == value and player == board[i]:
                count += 1
        return count
    else:
        for i in board:
            if i[1] == value and player == board[i]:
                count += 1
        return count
    


def nearest_piece(board,x,y):
    sum = 1000000
    for i in board:
        if (abs(x - i[0]) + abs(y - i[1])) < sum:
            sum = (abs(x - i[0]) + abs(y - i[1]))
    if sum == 1000000:
        return False        
    else: 
        for i in board:
            if (abs(x - i[0]) + abs(y - i[1])) == sum:
                return i
            

def choose(n,k):
    if k > (n-k):
        return fact(n,k)//fact(n-k)
    else: 
        return fact(n,n-k)//fact(k)

def fact(n,k=1):   
    if n == k:
        return 1
    else:
        return n * fact(n-1, k)
    



        
