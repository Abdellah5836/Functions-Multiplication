from fractions import Fraction

frac_info = {}
hexa_info = {}
multip_func = {}

def simple_frac(frac_info, hexa_info, multip_func):
	"""simple Fraction equation"""
	query = input("Enter the number of hex you have: ")
	num2 = int(query)
	num1 = 1
	while num1 <= num2:
		numera = input("Enter a numeratur: ")
		denamina = input("Enter a denamenator: ")
		message = input("Does your function contain mixed numbers? ('y' or 'n')")
		if message.lower() == 'y':
			mixed_num = input("Enter the mixed number here: ")
			hexa_info['mixed number'] = int(mixed_num)
			print("\t\tAdding Info...")
			hexa_info['numerator'] = int(numera)
			hexa_info['denamenator'] = int(denamina)
			frac_info['hexa_info'] = f"{hexa_info}"
	
			hexa = Fraction(((int(mixed_num) * int(denamina)) + int(numera)), int(denamina))
			multip_func[num1] = f"{hexa}"

		if message.lower() == 'n':
			print("\t\tAdding Info...")
			hexa_info['numerator'] = int(numera)
			hexa_info['denamenator'] = int(denamina)
			frac_info['hexa_info'] = f"{hexa_info}"
	
			hexa = Fraction(int(numera), int(denamina))
			multip_func[num1] = f"{hexa}"

		print(f"this is: {multip_func}")
	
		
		num1 += 1
	
		


def multi_frac(multip_func):
	list_1 = []
	for v in multip_func.values():
		num_frac = Fraction(v)
		list_1.append(num_frac)
	print(list_1)
	
	def multi_nums(list_1):
		n = 1
		for x in list_1:
			n = n * x
		print("The product would be:")
		return n

	print(multi_nums(list_1))

simple_frac(frac_info, hexa_info, multip_func)
multi_frac(multip_func)

