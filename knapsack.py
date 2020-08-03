import time

def knapSack(W, wt, val, n): 
  
    if n == 0 or W == 0 : 
        return 0

    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 

    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),  knapSack(W, wt, val, n-1))


val = [23, 45, 25, 92, 44, 65, 38, 73, 94, 85, 12, 36, 16, 77, 66, 45, 56, 99, 72, 89, 91, 38, 78, 45, 60, 51, 0, 87, 63, 88, 62, 51] 
weight = [6, 2, 9, 8, 4, 8, 3, 9, 10, 9, 3, 7, 4, 1, 2, 8, 0, 5, 5, 0, 3, 3, 8, 1, 2, 1, 2, 5, 6, 6, 2, 9] 
maxim = 65

zipped_lists = zip(val, weight)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
val, wt = [ list(tuple) for tuple in  tuples]


male = val[:len(val)//2]
female = val[len(val)//2:]

weight1 = wt[:len(weight)//2]
weight2 = wt[len(weight)//2:]

n1 = len(male)
n2 = len(female)


avg1 = int(sum(male)/len(male))
avg2 = int(sum(female)/len(female))

totalw = avg1+avg2

max1 = round(avg1/totalw*maxim)
max2 = round(avg2/totalw*maxim)


startknap = time.time()
first = knapSack(max1, weight1, male, n1)
second = knapSack(max2, weight2, female, n2)
total = first+second

print(avg1)
print(avg2)
print("\n")
print(max1)
print(max2)
print("\n")
print(male)
print(weight1)
print("\n")
print(female)
print(weight2)
print ("\n\nFirst half : ", first)
print ("Second half : ", second)
print("Optimal : " , total)
endknap = time.time()

print("Time for solving knapsack: ", endknap-startknap)
