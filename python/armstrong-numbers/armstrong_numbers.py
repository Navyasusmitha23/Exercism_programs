def is_armstrong_number(number):
     str_num = str(number)
     power = len(str_num)
     char_list = list(str_num)
     digit_sum = 0
     for i in char_list:
         digit_sum += int(i)**power
     if digit_sum == number:
        return True
     else:
         return False
