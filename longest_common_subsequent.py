'''
Longest Common subsequent
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Example 1:

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
''''

str1 = 'ABCDGH'
str2 = 'AEDFHR'

lst2 = re.split('', str2)

candidate =[]

for ele in str1:
    if ele in lst2:
        candidate.append(ele)

print(''.join(candidate))