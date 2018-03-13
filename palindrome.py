import sys

def handle_opt(argv):

	if len(argv) != 2:
		print("usage: palindrome.py int")
		sys.exit(1)

	else:
		try:
			out_value = int(argv[1])
			return out_value

		except ValueError:
			print("Type Error: sequence_length must be an integer")
			sys.exit(1)

def is_palindrome(num):

	num = str(num)
	if(len(num) % 2 == 0):
		for i in range(0, len(num) - 1, 1):
			for y in range(len(num) - 1, 0, -1):
				first = num[i]
				last = num[y]
				if (first != last):
					return False
		return True
	else:
		i = 0
		y = len(num) - 1

		while(i != y):
			if(num[i] != num[y]):
				return False
			i += 1
			y -= 1
		return True

def check_upper(palindrome, distance):

	for i in range(palindrome, distance + palindrome):
		if(is_palindrome(i) == True):
			return i
	return False

def find_palindrome(number):

	for i in range(0, number):
		if(is_palindrome(i) == True):
			palindrome = i

	distance = number - palindrome
	upper = check_upper(number, distance)

	if(upper != False):
		return upper
	else:
		return palindrome

def main():

	number = handle_opt(sys.argv)
	print(number)

	palindrome = find_palindrome(number)
	print("Your closest palindrome is " + str(palindrome))

if __name__ == "__main__":
	main()