
def num_system():
	"""Adding positive and negative whole numbers"""
	list_of_nums = []
	while True:
		print("Enter 'q' whenever you want to quit.")
		print("Would you like to know the sum of two numbers?")
		num1 = input("Enter an Integer:")
		if num1.lower() == 'q':
			break
		num2 = input("Enter another Integer: ")
		if num2.lower() == 'q':
			break
		num_1 = int(num1)
		num_2 = int(num2)
		list_of_nums.append(num_1)
		list_of_nums.append(num_2)
		print(list_of_nums)

		if (int(num_1) > 0) and (int(num_2) > 0):
			sum = int(num_1) + int(num_2)
			print("bothe numbers are positives")
			return sum

		if (int(num_1) < 0) and (int(num_2) < 0):
			sum = int(num_1) + int(num_2)
			print("both numbers are negatives!")
			return sum

		if (int(num_1) < 0) or (int(num_2) < 0):
			sum = abs(int(num_1)) - abs(int(num_2))
			if (num_1 < 0) and (abs(num_1) > abs(num_2)):
				print("the first number is negative, but it's greater than the second number!")
				return sum * (-1)

			if (num_1 < 0) and (abs(num_1) < abs(num_2)):
				print("the first number is negative, but it's smaller then the second number!")
				return sum * (-1)

			if (num_1 > 0) and (abs(num_1) < abs(num_2)):
				print("the first number is positive, but it's smaller then the second number!")
				return sum

			if (num_1 > 0) and (abs(num_1) > abs(num_2)):
				print("the first number is positive, but it's greater then the second number!")
				return sum


res = ns()
print(f"\nSum is: {res}")
