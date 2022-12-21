# this function replaces the None values of a list with the most repeated value in a list

def fill_none():
    
    n = int(input("enter the number of elements: "))
    
    lst_num = []
    counts = []
    
    for i in range(0, n):
        ele = input()
        lst_num.append(ele)
    
    print('The input list is: ', lst_num)
    
    lst_num2 = lst_num
    
    while None in lst_num:
        lst_num.remove(None)
    
    for ele in lst_num:
        counts.append(lst_num.count(ele))
    
    idx = counts.index(max(counts))
    most_frequent = lst_num[idx]
    
    print('The most frequent element of the list is: ', most_frequent)
    
    for ele in lst_num2:
        if ele == 'None':
            print(ele)
            none_index = lst_num2.index(ele)
            print('The index of none element: ', none_index)
            lst_num2[none_index] = most_frequent
    
    print(lst_num2)
    
if __name__ == '__main__':
    fill_none()
