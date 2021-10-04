from tree import Node
from copy import deepcopy

stack = []
queens_num = 8
amountStates = 0

dom = [ [ i for i in range(0,queens_num) ] for _ in range(0,queens_num) ]

def start(currentNode, currentDomain, queens_num):
    currentRow = (currentNode.height+1)
    if((currentNode.height+1) == queens_num):
        result = currentNode.pathToRoot()
        result.pop()
        result.reverse()
        return (result,amountStates)
    else:
        for i in range(0,len(currentDomain[currentRow])):
            newDomains = deepcopy(currentDomain)
            newNode = Node(currentDomain[currentRow][i],currentRow,currentNode)
            newDomains[currentRow] = [currentDomain[currentRow][i]]
            revise(newNode, newDomains)
            if(newDomains == False):
                return None
            result = start(newNode,newDomains,queens_num)
            if(result != None):
                return (result,amountStates)
    return None


def revise(currentNode, newDomains):
    global stack, queens_num, amountStates
    col = currentNode.value
    height = currentNode.height
    amountStates += 1
    for i in range(0,len(newDomains)):
        domain = newDomains[i]
        lengthDomain = len(domain)
        j = 0
        while j < (lengthDomain):
            currentValue = domain[j]
            if(i != height):
                if(currentValue == col):
                    domain.remove(col)
                    j -= 1
                    lengthDomain -= 1
                elif(abs(currentValue-col) == abs(i-height)):
                        domain.remove(currentValue)
                        j -= 1
                        lengthDomain -= 1
            j = j+1
        if(len(domain) == 0):
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

