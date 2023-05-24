from itertools import combinations_with_replacement

N = 43
lst=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

big_lst = []

for i in range(len(lst)):
    big_lst.append(list(combinations_with_replacement(lst, i)))

selected_lst = []

for lst in big_lst:
    for ele in lst:
        if ele !=() and sum(ele)==N:
            selected_lst.append((ele))

min_length = len(selected_lst[0])
candidate=selected_lst[0]

for ele in selected_lst:
    length = len(ele)
    if length < min_length:
        min_length = length
        candidate=ele 
