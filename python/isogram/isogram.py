def is_isogram(string):
    string = string.lower()
    seen_char = set()
    for char in string:
        #if char.isalpha() and string.count(char)>1:
        if char.isalpha():
           if char in seen_char:
              return False
           seen_char.add(char)
    return True
           
