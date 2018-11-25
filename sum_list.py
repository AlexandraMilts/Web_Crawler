def first_sum(items):
	result = 0
	for item in items:
		result += item
	return result


def second_sum(items):
	result = 0
	for item in items:
		result += item
	print(result)


print("first call will not print anything .. function returns a value but we do nothing with it")
first_sum([1, 4, 7])
print("second call will print the value .. function returns a value and we print it")
print(first_sum([1, 4, 7]))
print('third call will print the value as a side-effect of calling the function itself')
second_sum([1, 4, 7])
print("fourth call will print the value as a side-effect of calling the function itself .. and the function call returns None .. which will be printed here")
print(second_sum([1, 4, 7]))
