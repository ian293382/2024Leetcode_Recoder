def fizzBuzz(n):
    rule = {3 : 'Fizz', 5: 'Buzz'}

    result =  [rule.get(3, '') * ( i % 3 == 0) +
              rule.get(5, '') * ( i % 5 == 0) or
              str(i)
              for i in range(1,n+1)] 
    return result

for i in range(1,101):
       print(*fizzBuzz(i))