import backtracking
from tree import Node
import forwardchecking
import time
queens_nums = [8]

backTrackingTime = []
backTrackingStates = []
forwardCheckingTime = []
forwardCheckingStates = []

for num in queens_nums:
    dom = [ [ i for i in range(0,num) ] for _ in range(0,num) ]
    root = Node(13,-1,None)
    start = time.time()
    result = forwardchecking.start(root,dom,num)
    end = time.time()
    forwardCheckingTime.append((end-start))
    forwardCheckingStates.append(result[1])

for num in queens_nums:
    start = time.time()
    result = backtracking.start(num)
    end = time.time()
    backTrackingTime.append((end-start))
    backTrackingStates.append(result[1])
    

print("8 queens Backtracking times", backTrackingTime)
print("8 queens Backtracking states", backTrackingStates)
print("8 queens Forward checking times", forwardCheckingTime)
print("8 queens Forward checking states", forwardCheckingStates)
