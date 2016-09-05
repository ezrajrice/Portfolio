"""
Author: Ezra Rice
Date: 5 September 2016

Note: Feel free to use this code as you wish. I just ask that 
      you give proper credit to the author for any replication 
      of code or algorithm. Thank you.
"""

# Take the entire code as a string from a file
encrypted_file = open('encrypted_file.txt', 'r')
decrypted_file = open('decrypted_file.txt', 'w')

encrypted_file_as_string = encrypted_file.read()

# Turn string into list of numbers
string_list = encrypted_file_as_string.split('.')
int_list = []
for current_string in string_list:
	if current_string != '':
		int_list.append(int(current_string))

chunked_list = []

# XECryption is chunks of 3 numbers that add up to the ASCII decimal value
# The sum value of the password characters is also divided into these 3 numbers that make up one chunk
index = 0
while index < len(int_list):
	num_one = int_list[index]
	num_two = int_list[index + 1]
	num_three = int_list[index + 2]

	chunked_list.append(num_one + num_two + num_three)
	index += 3

# Get the minimum number in the list and compare it to valid ASCII characters
min_int = min(chunked_list)

password_value = 0
while password_value <= min_int:
	invalid_count = 0
	for character in chunked_list:
		if character - password_value not in range(32, 126):
			invalid_count += 1
	if invalid_count <= 15:
		for character in chunked_list:
			current_character = chr(character - password_value)
			decrypted_file.write(current_character)
		decrypted_file.write('\n\n--------------------------------------------\n\n')
	password_value += 1
	# print(invalid_count)
decrypted_file.write("End of script.")
encrypted_file.close()
decrypted_file.close()
