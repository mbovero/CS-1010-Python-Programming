#Miles Bovero
#Period 3




VOWELS = "aeiou"
END = ".,!?"

def way_end(word):
	if word[-1] in END:
		return f"{word[:-1]}way{word[-1]}"
	else:
		return f"{word}way"

def ay_end(word,index):
	if word[-1] in END:
		return f"{word[index:-1] + word[:index]+'ay'+word[-1]}"
	else:
		return f"{word[index:] + word[:index]+'ay'}"

def read(file):
	document = open(f"{file}", "r")
	lines = document.readlines()
	list = []
	try:
		open(f"{file}", "r")
		for line in lines:
			list.append(f"{line}")
		return list
	except IOError:
		return ["1error"]
	finally:
		document.close()



def write(new):
	document = open("pig.txt", "w")
	for line in new:
		document.write(f"{line}")
	document.close()


def translate(message):
	pig = []
	for line in message:
		line = line.strip()
		words = line.split(" ");
		new = []
		for word in words:
			if word[0] in VOWELS:
				new.append(way_end(word.lower()))
			elif word[0].isalpha():
				for letter in word:
					if letter in VOWELS:
						index = word.index(letter)
						new.append(ay_end(word.lower(),index))
						break
			else:
				new.append(word.lower())
		pig.append(" ".join(new) + '\n')
	return pig


def main():
	print("Welcome to the Pig Latin Translator!")
	file = input("What is the name of the file:\n")
	message = read(file)
	new = translate(message)
	write(new)
	print("Message stored in 'pig.txt'")

if __name__ == "__main__":
	main()
