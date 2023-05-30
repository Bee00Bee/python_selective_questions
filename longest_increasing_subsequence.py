'''
Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example 1:

Input:
N = 16
A[]={0,8,4,12,2,10,6,14,1,9,5
     13,3,11,7,15}
Output: 6
Explanation:Longest increasing subsequence
0 2 6 9 13 15, which has length 6
Example 2:

Input:
N = 6
A[] = {5,8,3,7,9,1}
Output: 3
Explanation:Longest increasing subsequence
5 7 9, with length 3
'''

#lst = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
lst=[5,8,3,7,9,1]
from itertools import combinations

big_lst = []

for i in range(len(lst)):
    big_lst.append(list(combinations(lst,i)))

def check_order(lst):
    lst_check = []
    if len(lst) > 1:
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst_check.append(True)

        if len(lst_check)==len(lst)-1:
            return True
        else:
            return False
        
candidate=[]
length=1
for lst in big_lst:
    for ele in lst:
        if check_order(list(ele)):
            if len(list(ele)) > length:
                candidate=list(ele)
                length=len(list(ele))
               
print(candidate)