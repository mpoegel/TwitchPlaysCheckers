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

	def watch_chat(self):
		while True:
			twitch_activity = self.irc.recv(4096)
			print twitch_activity
			
			if twitch_activity.isspace():
				return

			if "PING" in twitch_activity:
				self.irc.send("PONG tmi.twitch.tv")
				print "PONG tmi.twitch.tv"

			# If the channel has receieved a twitch chat message
			if "PRIVMSG" in twitch_activity:

				# extract the contents of the message
				i = twitch_activity[1:].find(":")
				message = twitch_activity[i+2:]
				command = message.split()

#################### MAIN - TEST ############################

if __name__ == '__main__':
	userInput = TwitchChatReader()
	userInput.watch_chat()