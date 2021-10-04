from tree import Node

stack = []
queens_num = 12
amountStates = 0

def start(queens_num):
    global stack, amountStates
    root = Node(13,-1,None)
    stack.append(root)
    while(len(stack) > 0):
        currentNode = stack.pop(0)
        amountStates += 1
        if((currentNode.height+1) == queens_num):
            result = currentNode.pathToRoot()
            result.pop()
            result.reverse()
            return (result,amountStates)
        for i in range(0,queens_num):
            if(check(currentNode,i,currentNode.height+1) == True):
                newNode = Node(i,(currentNode.height+1),currentNode)
                stack.append(newNode)

def check(currentNode,col,height):
    global stack, queens_num
    currentPositions = currentNode.pathToRoot()
    for i in range(0,len(currentPositions)):
        currentQueen = currentPositions[i]
        if(currentQueen[0] == col):
            return False
        if(abs(currentQueen[0]-col) == abs(currentQueen[1]-height)):
            return False
    return True

def printQueens(path):
    board = [ [ "*" for _ in range(0,queens_num) ] for _ in range(0,queens_num) ]
    for i in range(0, queens_num):
        currentPos = path[i]
        board[currentPos[0]][currentPos[1]] = "o"
    for i in range(0, queens_num):
        for j in range(0, queens_num):
            print(board[i][j],end="")
        print("")
