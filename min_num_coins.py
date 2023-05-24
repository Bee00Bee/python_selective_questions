'''You are given N pairs of numbers. In every pair, the first number is always smaller than the second number. 
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. 
You have to find the longest chain which can be formed from the given set of pairs. '''

if __name__=='__main__':
    
    lst = [(5, 24) , (70, 60) , (15, 28) , (20, 40) , (100, 90)]
    lst2=[]
    count = 0
    
    for ele in lst:
        if ele[0] < ele[1]:
            count += 1

        if ele[0] > ele[1]:
            lst2.append(count)
            count = 0

    lst2.append(count)

    print(max(lst2))
