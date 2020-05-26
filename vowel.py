def vow(string,vowels):
	final=[each for each in string if each in vowels]
	print(len(final))
	print(final)
string="Git Hub Program"
vowels="AaEeIiOoUu"
vow(string,vowels)
	