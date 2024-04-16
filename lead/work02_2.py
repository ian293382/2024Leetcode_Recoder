x = input('please enter 123') 
y = input('please enter 456.789')

x = float(x)
y = float(y)
sum = x + y
print(type(sum)) if isinstance(sum, float) else print('you answered with the wrong datatype')

print(sum)