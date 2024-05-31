def abbreviate(words):
    words= words.replace('-',' ').replace('_',' ')
    word_list = words.split()
    acronym=''
    for word in word_list:
        first_letter = word[0].upper()
        acronym += first_letter
    return acronym
    
    
     # return ''.join(word[0].upper() for word in words.replace('-',' ').replace('_',' ').split())
    