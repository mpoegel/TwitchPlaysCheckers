import socket
import sys

class TwitchChatReader():
	def __init__(self):
		self.server = "irc.twitch.tv"
		self.password = "oauth:8nq3rymmy4zakeut4p90hx9axnpywj"
		self.nickname = "twitchlosescheckers"
		self.channel = "#twitchlosescheckers"
		self.irc = None

		try:
			self.irc = socket.socket()
		except socket.error as msg:
			self.irc = None

		try:
			self.irc.connect((self.server, 6667))
		except socket.error as msg:
			self.irc.close()
			self.irc = None

		if self.irc is None:
			print "could not open socket"
			sys.exit()

		self.irc.send('PASS ' + self.password + '\n')
		self.irc.send('NICK ' + self.nickname + '\n')
		self.irc.send('JOIN ' + self.channel + '\n')

	def read_chat(self):
		while True:
			twitch_activity = self.irc.recv(4096)
			print twitch_activity
			
			if "PING" in twitch_activity:
				self.irc.send("PONG tmi.twitch.tv\n")
				print "PONG tmi.twitch.tv"

			# If the channel has receieved a twitch chat message
			if "PRIVMSG" in twitch_activity:

				# extract the contents of the message
				i = twitch_activity[1:].find(":")
				message = twitch_activity[i+2:]
				command = message.strip().split()

				if len(command) == 2:
					alphabet = " ABCDEFGH"	
					if len(command[0]) == 2:
						if command[0][0].isalpha():	
							r0 = alphabet.find(command[0][0].upper())
							if r0 == 0:
								continue
							print "r0 = %d" %(r0)
						else:
							continue

						if command[0][1].isdigit() and 1 <= int(command[0][1]) <= 8:
							c0 = int(command[0][1])
							print "c0 = %d" %(c0)
						else:
							continue
					else:
						continue

					if len(command[1]) == 2:
						if command[1][0].isalpha():
							r1 = alphabet.find(command[1][0].upper())
							if r1 == 0:
								continue
							print "r1 = %d" %(r1)
						else:
							continue

						if command[1][1].isdigit() and 1 <= int(command[1][1]) <= 8:
							c1 = int(command[1][1])
							print "c1 = %d" %(c1)
						else:
							continue
					else:
						continue

					return (r0, c0), (r1, c1)

	def stop(self):
		self.irc.close()

#################### MAIN - TEST ############################
'''
if __name__ == '__main__':
	userInput = TwitchChatReader()
	while(True):	
		nextMove = userInput.read_chat()
		print "MOVE COMMAND: %s" %(str(nextMove))

	userInput.stop()
'''