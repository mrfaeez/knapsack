#THIS IS A CODE FOR  SENTINELS TO FIND THE BEST WAY TO TAKE THE MUTANS
#THE CODE IS A COMBINATION OF KNAPSACK AND SOCIAL SPIDER OPTIMIZATION



import time


#divided subroutine of calculating the knapsack using recursion
def knapSack(W, wt, val, n): 
  
    if n == 0 or W == 0 : 
        return 0

    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 

    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),  knapSack(W, wt, val, n-1))


#initialize the value and weight of the mutans
val = [23, 45, 25, 92, 44, 65, 38, 73, 94, 85, 12, 36, 16, 77, 66, 45, 56, 99, 72, 89, 91, 38, 78, 45, 60, 51, 0, 87, 63, 88, 62, 51] 
weight = [6, 2, 9, 8, 4, 8, 3, 9, 10, 9, 3, 7, 4, 1, 2, 8, 0, 5, 5, 0, 3, 3, 8, 1, 2, 1, 2, 5, 6, 6, 2, 9] 
maxim = 65


#sort both array respectively, as it is related
zipped_lists = zip(val, weight)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
val, wt = [ list(tuple) for tuple in  tuples]


#divide the mutans to 2 gender of spider which is male and female
male = val[:len(val)//2]
female = val[len(val)//2:]

weight1 = wt[:len(weight)//2]
weight2 = wt[len(weight)//2:]

n1 = len(male)
n2 = len(female)


#calculate the average of both lists divided
avg1 = int(sum(male)/len(male))
avg2 = int(sum(female)/len(female))

totalw = avg1+avg2


#set the best capacity for each list, according to the gender of spider
max1 = round(avg1/totalw*maxim)
max2 = round(avg2/totalw*maxim)


#start finding the best value for each of the list
startknap = time.time()
first = knapSack(max1, weight1, male, n1)
second = knapSack(max2, weight2, female, n2)
total = first+second
endknap = time.time()


#display the output and finding of the sloved knapsack
print ("\nMale spider : ", first)
print ("Female spider : ", second)
print("\nThe best optimal solution for finding the mutans : " , total)
print("\n\nTime for solving knapsack problem: ", endknap-startknap)
