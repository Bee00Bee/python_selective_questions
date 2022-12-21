# this function prints out the character in a string which appears more than once.

def find_char():
    string = input()
    count_lst = []
    for char in string:
        count = string.count(char)
        if count > 1:
            print(string.index(char))
        else:
            print(-1)
        
if __name__ == '__main__':
    find_char()
