# this function moves all zeros of list to the end of it

def move_zeros():
    
    n = input()
    
    non_zero = []
    zeros = []
    lst_num = []
    
    for i in range(len(n)):
        lst_num.append(int(n[i]))
    
    for i in range(len(lst_num)):
        if lst_num[i] != 0:
            non_zero.append(lst_num[i])
        elif lst_num[i] ==0:
            zeros.append(lst_num[i])
            
    final_lst = non_zero+zeros
    print(final_lst)
    
if __name__ == '__main__':
    move_zeros()
