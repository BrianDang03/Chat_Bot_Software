from irc_interface import TalkToClient

def EnsureHashtag(s):
    if not s.startswith("#"):
        return "#" + s
    return s

def main():
    # Prompt User
    ipAddress = input("Enter IP Address: ")
    portNumber = input("Enter Port Number: ")
    channel = input ("Enter a Channel: ")
    channel = EnsureHashtag(channel)

    # Talk to Client
    TalkToClient(ipAddress, int(portNumber), channel)
    
main()