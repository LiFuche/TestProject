word_list = []

def add_word(word):
	global word_list
	if word in word_list:
		print("this word has already existed.")
	else:
		word_list.append(word)
		print("add word successful.")

def find_word(word):
	global word_list
	if word in word_list:
		print(word)
	else:
		print("can't find the word.")

def  del_word(word):
	global word_list
	if word in word_list:
		word_list.remove(word)
	else:
		print("can't find the word.")

if __name__ == "__main__":
	print("=======a:add word=======\n=======f:find word=======\n=======d:delete word=======\n=======bye:exit=======")
	while 1:
		command = input("please input a command:")
		if command == "a":
			word = input("please input the word you want to add:")
			add_word(word)
		elif command == "f":
			word = input("please input the word you want to find:")
			find_word(word)
		elif command == "d":
			word = input("please input the word you want to delete:")
			del_word(word)
			print("delete successful!")
		elif command == "bye":
			break
		else:
			command = print("Incorrect command,", end="")