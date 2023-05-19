from itertools import product, permutations

A = [3, 1, 2]
B = [6, 5, 4]

if __name__ == '__main__':

    dic = {}
    lst_2 = []
    for ele in A:
        lst = []
        for ele2 in B:
            lst.append(ele*ele2)
        lst_2.append(lst)

    products = []
    products = list(product(*lst_2))

    min = sum(products[0])

    for ele in products:
        if sum(ele) < min:
            dic = {}
            min = sum(ele)
            dic[ele] = min

    print(f'The minumum sum is: ', list(dic.values())[0])