'''
In a candy store, there are N different types of candies available and the prices of all the N different types
of candies are provided to you. You are now provided with an attractive offer.
For every candy you buy from the store and get at most K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to find what is the minimum amount of money you have 
to spend to buy all the N different candies. Secondly, you have to find what is the maximum amount of money you
have to spend to buy all the N different candies. In both the cases you must utilize the offer i.e. 
you buy one candy and get K other candies for free.
'''

if __name__=="__main__":
    print('Give the number of candies: ')
    N=int(input())
    print('Provide the candies prices: ')
    candies=[]
    [candies.append(int(input())) for i in range(N)]
    print('The list of candies prices are: ', candies)
    print('How many candies do you want to pick? ')
    K=int(input())

    candies.sort()
    
    minimum_prices= candies[:-K]
    print(f'minimum price: ', sum(minimum_prices))

    maximum_prices = candies[K:]
    print(maximum_prices)
    print(f'maximum price: ', sum(candies[K:]))