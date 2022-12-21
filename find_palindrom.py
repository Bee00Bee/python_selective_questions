# this finds a palindrom by removing only one character from the string

def find_palindrom():
    string = input()
    reversed_string = string[::-1]
    
    true_false = []
    
    if string == reversed_string:
        print(True)
    else:
        for i in range(len(string)):
            true_false.append(string[i]==reversed_string[i])
        if False in true_false:
            idx = true_false.index(False)
            lst_string = list(string)
            lst_string.pop(idx)
            new_string = ''.join(lst_string)
            if new_string == new_string[::-1]:
                print('modified string:', new_string)
                print(True)
        
if __name__ == '__main__':
    find_palindrom()
