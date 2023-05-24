'''
 longest common substring

Given two strings. The task is to find the length of the longest common substring.


Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.
Example 2:

Input: S1 = "ABC", S2 "ACB", n = 3, m = 3
Output: 1
Explanation: The longest common substrings
are "A", "B", "C" all having length 1.
'''

if __name__ == "__main__":

    S1 = "ABCDGH"; S2 = "ACDGHR"

    lst1=[]; lst2=[]
    [lst1.append(ele) for ele in S1]
    [lst2.append(ele) for ele in S2]

    words = ''
    for ele in lst1:
        if ele in lst2:
            words += ele
        elif ele not in lst2:
            words += ' '

    lst_words=[]

    lst_words = words.split(' ')

    max_len = len(lst_words)
    candidate = lst_words[0]

    for ele in lst_words:
        if len(ele) > max_len:
            candidate=ele
            max_len=len(ele)
