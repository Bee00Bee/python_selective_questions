# this function checks whether or not the given number is a prime number

def check_prime_num():
    
    num = int(input())
    
    count = 0
    
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
            
    if count <=2:
        print(num, ' is a prime number')
    else:
        print('This number: ', num, ' is not a prime number')
        
        
if __name__ == '__main__':
    check_prime_num()
