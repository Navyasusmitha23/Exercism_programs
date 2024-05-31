def is_valid(isbn):
    isbn = isbn.replace('-','')
    if len(isbn)!=10: 
       return False
    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
           return False
        total += int(isbn[i])*(i+1)

    if isbn[9] == 'X':
       total += 10*10
    elif isbn[9].isdigit():
        total += int(isbn[9])*10
    else: 
         return False

    return total%11 == 0