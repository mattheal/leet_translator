#leet translator special thanks to usingpython.com

print("Welcome to the 133t translator!")
print("-------------------------------")
print()
print()

leet = {"a":"4","b":"l3","c":"(","d":"[)","e":"3","g":"6","l":"1","o":"0","s":"5","t":"7","w":"\/\/"}

new_leet= {b:a for a,b in leet.items()}
new_leet_list = [new_leet[key] for key in new_leet]

#The initilization function allows the user to choose between english to leet or leet to 
#english
def __init__():
	choice = input("Would you like to translate from leet to English or English to leet? [l for leet e for english ")
	choice = choice.lower()
	if choice[0] == 'l':
		print(leet2eng())
	elif choice[0] == 'e':
		print(eng2leet())
	else:
		print("Sorry you have to press 'e' for english 'l' for leet, you pressed ",choice)

#this function takes the users english input and translates it to leet
def eng2leet():
	textOut=[]
	textIn=input("Give us a statement to translate: ")

	for char in textIn:
		if char in leet:
			textOut.append(leet[char])
		else:
			textOut.append(char)

	myOut = "".join(textOut)
	print(myOut)

#this function takes the users leet input and transl
def leet2eng():
	textOut=[]
	textIn=str(input("Give us a statement to translate: "))

	for char in textIn:
		if char in new_leet:
			textOut.append(new_leet[char])
			print("test character is: ",char)
		else:
			textOut.append(char)

	myOut = "".join(textOut)
	print(myOut)

__init__()
