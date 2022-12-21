# this function checks whether or not a list of number is monotonic

def check_monotonic():
     n = input()
     lst=[]
     for i in range(len(n)-1):
         print(n[i], n[i+1])
         if n[i] < n[i+1]:
             lst.append(True)
         else:
             lst.append(False)
     if False not in lst:
         print('The array is Monotonic')
     else:
        print('The array is not Monotonic')
     
                    
if __name__== '__main__':
    check_monotonic()
