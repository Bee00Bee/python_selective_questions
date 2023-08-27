def reverse_integer(lst):
    return list(reversed(lst))


if __name__=="__main__":
    lst = str(input())
    print('list of numbers: ', lst)
    print(reverse_integer(lst))
