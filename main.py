import random

lucky_number = random.randint(1,100)
fortune_number = random.randint(1,4)
fortune_phrase = ''

if fortune_number == 1:
  fortune_prase = 'You will have a great day!'
if fortune_number == 2:
  fortune_phrase = 'I wish you a pleasant diharrea'
if fortune_number == 3:
  fortune_phrase = 'You will get married this year'
if fortune_number == 4:
  fortune_phrase = 'You will get a new car this year'

print(f"your lucky number is {lucky_number} and your fortune is {fortune_phrase}")