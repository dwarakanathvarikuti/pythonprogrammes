input = input("Enter a number between 0.0 and 1.0:")
score = float(input)
if (score>=1.0):
	print("you didnt follow the instructions")
	exit()
elif(score >=0.9):
	print('A')
elif(score >=0.8):
	print('B')
elif(score >=0.7):
	print('c')
elif(score >=0.6):
	print('D')
else:
	print('F')
print("please enter numerical numbers")
exit()