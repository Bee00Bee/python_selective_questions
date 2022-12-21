# this function finds the most common words in two different strings

def find_common_words():
    
    string_1 = input()
    string_2 = input()
    
    lst_word_1 = string_1.split(' ')
    lst_word_2 = string_2.split(' ')
    
    if set(lst_word_1) & set(lst_word_2):
        print(set(lst_word_1) & set(lst_word_2))
   
        
    
if __name__ == '__main__':
    find_common_words()
