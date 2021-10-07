x =[10, 40, 30, 50, 20]
w= [1, 2, 3, 4, 5]
def weightedMean(x, w):
    # Write your code here
    i = 0
    sum_weight = 0
    persons = 0
    while i < len(x):
        sum_weight +=x[i] * w[i]
        persons+=w[i]
        i += 1
    output = round(sum_weight/persons,1)
    print(output) 

