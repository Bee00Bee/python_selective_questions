'''
Coin Change

Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. 


Example 1:

Input:
sum = 4 , 
N = 3
coins[] = {1,2,3}
Output: 4
Explanation: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.'''

from itertools import combinations_with_replacement


if __name__=='__main__':
    print('Provide the number of coins:')
    length = int(input())
    coins=[]
    print('give the coins:')
    for i in range(0, length):
        coins.append(int(input()))
    print('What must be the sum of coins?')
    total = int(input())

    print(f'\nHere is the list of coins: {coins} and the sum must be: {total}')

    print('\nThe combinations of coins are:')
    count = 0
    for i in range(1, total+1):
        lst = combinations_with_replacement(coins,i)
        lst2=list(lst)
        for ele in lst2:
            if sum(ele)==total:
                print(ele)
                count += 1
    print(f'\nThe number of combinations is: {count}')