# Erste Möglichkeit
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i) 


#Zweite Möglichkeit
for i in range(1, 101):
  output = "" 
  if i % 3 == 0:
    output = "Fizz"

  if i % 5 == 0:
    output = output + "Buzz"
  
  if len(output) == 0:
    output = i

  print(output)