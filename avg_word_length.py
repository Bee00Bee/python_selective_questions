# this function calculates the average word lengths in a string

def word_avg_length():
    
    text = input()
    
    char_lst = ['.', '...', '>', '<', '?', ',', '"', '[', ']', '!']
    new_text = ''
    
    for ele in char_lst:
        text = text.replace(ele, ' ')
        
    print('clean text\n', text)
    
    words = []
    words = text.split(' ')
    
    length = 0
    for word in words:
        if word != '':
            print(len(word))
            length += len(word)
    
    num_words = len(words) - words.count('')
    print('\navg of word lengths\n', length/num_words)
    print('The number of words are: ', num_words)
    


if __name__ == '__main__':
    word_avg_length()
