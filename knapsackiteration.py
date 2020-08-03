import time


def knapSack(W, wt, val, n):
    result
    While True:
        
        if n==0 or W == 0 :
            break

        if wt[n-1] > W:
            n -= 1

        elif :
            first = val[n-1] + 
            


    
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 

startknap = time.time()

total = knapSack(maxim, weight, val, n)


print("Optimal : " , total)
endknap = time.time()

print("Time for solving knapsack: ", endknap-startknap)
