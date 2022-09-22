#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile #true is returned if they have the same facial expression and false if we are fine(they are not the same)

#Test Cases
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False