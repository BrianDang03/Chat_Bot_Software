from irc_interface import TalkToClient

def main():
    ipAddress = input("Enter IP Address: ")
    portNumber = input("Enter Port Number: ")
    channel = input ("Enter a Channel: ")
    TalkToClient(ipAddress, str(portNumber), channel)
main()