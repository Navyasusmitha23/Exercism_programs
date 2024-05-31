def commands(binary_str):
    actions = ['wink','double blink','close your eyes','jump']
    number = int(binary_str,2)

    hand_shake = []
    for i,bit in enumerate(reversed(binary_str)):
        if bit == '1':
           if i==4:
              hand_shake.reverse()
           else:
                 hand_shake.append(actions[i])
    return hand_shake     
             
    
  
               