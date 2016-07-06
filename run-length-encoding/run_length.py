def encode(string_arg):
	tmp = ''
	base_letter = string_arg[0]
	current_letter_count = 0
	for n, char in enumerate(string_arg, 1):
		if char == base_letter:
			current_letter_count += 1
		else:
			if current_letter_count is not 1:
				tmp += str(current_letter_count)
			tmp += base_letter
			base_letter = char
			current_letter_count = 1
		if n == len(string_arg):
			if current_letter_count is not 1:
				tmp += str(current_letter_count)
			tmp += base_letter
	return tmp
		
def decode(string_arg):
	tmp = ''
	multiplier = ''
	for n, char in enumerate(string_arg, 1):	
		if char.isdigit():
			multiplier += char
			continue
		if multiplier == '':
			tmp += char
		else:
			tmp += char * int(multiplier)
		multiplier = ''
	return tmp

if __name__ == '__main__':
	print(encode('AABBBCCCC'))
	print(decode('12WB12W3B24WB'))
