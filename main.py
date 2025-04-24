from irc_interface import TalkToClient

def main():
    # Prompt User
    ipAddress = input("Enter IP Address: ")
    portNumber = input("Enter Port Number: ")
    channel = input ("Enter a Channel: ")

    # Talk to Client
    TalkToClient(ipAddress, int(portNumber), channel)
main()