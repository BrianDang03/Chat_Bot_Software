import socket
import time
from gpt_connect import askGPT 

def TalkToClient(server, port, channel):
    """
    Resizes all images in a folder to the specified dimensions, overwriting the originals.
    
    Parameters:
    - server: should be an IP Address  
    - port: should be a port number
    - channel: #name channel to connect to  
    """

    # Configuration
    nickname = "ChatBot"
    username = "chatbot"
    realname = "Python IRC Bot"
                 
    # Create and connect socket
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))

    # Send NICK and USER to register
    irc.send(f"NICK {nickname}\r\n".encode("utf-8"))
    irc.send(f"USER {username} 0 * :{realname}\r\n".encode("utf-8"))

    # Join the channel after registration
    joined = False

    try:
        while True:
            resp = irc.recv(2048).decode("utf-8", errors="ignore")
            print(resp)

            # Respond to server PINGs
            if resp.startswith("PING"):
                irc.send(f"PONG {resp.split()[1]}\r\n".encode("utf-8"))

            # Wait for either end of MOTD (376) or no MOTD (422)
            if (" 376 " in resp or " 422 " in resp) and not joined:
                irc.send(f"JOIN {channel}\r\n".encode("utf-8"))
                time.sleep(1)
                irc.send(f"MODE {channel} +nt\r\n".encode("utf-8"))
                joined = True

            # If someone sends a message to the channel
            if f"PRIVMSG {channel}" in resp:
                sender = resp.split("!")[0][1:]
                message = ':'.join(resp.split(':')[2:]).strip()
                print(f"{sender}: {message}")
                                                  
                # Respond with a response message
                responseMsg = "Hello There"
                irc.send(f"PRIVMSG {channel} :{responseMsg}\r\n".encode("utf-8"))

    except KeyboardInterrupt:
        print("Disconnected.")
        irc.close()