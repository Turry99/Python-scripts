#This will be to count the vowels in a string and return how many times that letter repeats.
def Vowel_Count(string):
	vowels = ['a','e','i','o','u']
	vowel_list = [char for char in string if char in vowels]
	dictionary = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
	for char in vowels:
		while True:
			try:
				vowel_list.remove(char)
				dictionary[char] += 1
			except:
				break
	print(dictionary)

#Example:
Vowel_Count('Turtles are cute.') #Inside joke
#Should return : {'e': 3, 'i': 0, 'o': 0, 'u': 2, 'a': 1}


#Check if the string provided by the user is a palindrome.

def Palindrome_Check(palindrome):
	if palindrome == palindrome[::-1]:
		print("Yes , it is a palindrome.")
	else:
		print("No , it is not a palindrome.")

#Examples:
Palindrome_Check('racecar') # ---> It is a palindrome
Palindrome_Check('Turtle')  # ---> It is not a palindrome