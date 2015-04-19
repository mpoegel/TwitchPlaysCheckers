import socket
import sys

server = "irc.twitch.tv"
password = "oauth:8nq3rymmy4zakeut4p90hx9axnpywj"
nickname = "twitchlosescheckers"
channel = "#twitchlosescheckers"

try:
	irc = socket.socket()
except socket.error as msg:
	irc = None

try:
	irc.connect((server, 6667))
	print "connected to %s" %(server)
except socket.error as msg:
	irc.close()
	irc = None

if irc is None:
	print "could not open socket"
	sys.exit()

irc.send('PASS ' + password + '\n')
irc.send('NICK ' + nickname + '\n')
irc.send('JOIN ' + channel + '\n')

while True:
	twitch_activity = irc.recv(4096)
	print twitch_activity
	
	if "PING" in twitch_activity:
		irc.send("PONG tmi.twitch.tv");

	# If the channel has receieved a twitch chat message
	if "PRIVMSG" in twitch_activity:

		# extract the contents of the message
		i = twitch_activity[1:].find(":")
		message = twitch_activity[i+2:]

irc.close()