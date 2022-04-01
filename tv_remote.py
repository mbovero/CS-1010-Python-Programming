#Miles Bovero
#Period 3

class Remote():
	def __init__(self):
		self.__channel = 3
		self.__volume = 5
	def __str__(self):
		 return f"Channel: {self.__channel}\nVolume: {self.__volume}"


	def volume_up(self):
		if self.__volume < 10:
			self.__volume += 1

	def volume_down(self):
		if self.__volume > 0:
			self.__volume -= 1

	def channel_up(self):
		if self.__channel == 100:
			self.__channel = 1
		else:
			self.__channel += 1

	def channel_down(self):
		if self.__channel == 1:
			self.__channel = 100
		else:
			self.__channel -= 1



	@property
	def channel(self):
		return self.__channel

	@channel.setter
	def channel(self, new_channel):
		try:
			num = int(new_channel)
			if int(new_channel) not in range(1,100):
				print(f"'{new_channel}' is out of the channel range")
			else:
				self.__channel = int(new_channel)
		except ValueError as error:
			print(f"Error: {error}\nExplanation: '{new_channel}' isn't a number")





def main():
	r = Remote()
	print(r)
	user = ''
	MENU = '''
vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit
'''
	while user != 'q':
		print(MENU)
		user = input("Select an option:\n")
		if user == 'vu':
			r.volume_up()
		elif user == 'vd':
			r.volume_down()
		elif user == 'cu':
			r.channel_up()
		elif user == 'cd':
			r.channel_down()
		elif user == 'set':
			r.channel = input("What channel?\n")
		elif user == 'v':
			print(r)
		elif user == 'q':
			print("Goodbye.")
		elif user == 'z':
			print(r)
		else:
			print(f"{user} is not a valid option")

if __name__ == '__main__':
	main()
