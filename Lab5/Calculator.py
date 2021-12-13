from ComplexNumbers import Complex


user_input = input("Type what you want to calculate (add space between operator, for example '2+3j * 3-1j') >> ")
print(user_input)
first_string, operation, second_string = user_input.split()
print(first_string)
print(operation)
print(second_string)
first_num = Complex.from_string(first_string)
second_num = Complex.from_string(second_string)

if operation == '+':
    result = first_num + second_num
elif operation == '-':
    result = first_num - second_num
elif operation == '*':
    result = first_num * second_num
elif operation == '/':
    result = first_num / second_num
else:
    raise RuntimeError("Invalid operator provided")

print(f"The result of {first_num} {operation} {second_num} is {result}")
