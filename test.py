import socket
import time

def main():
    # Server details (change to match your real IP or DNS if not localhost)
    server = "irc.example.org"
    port = 6667
    nickname = "PyBot123"
    realname = "Python IRC Bot"
    channel = "#Help"

    # Create a socket connection
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))

    # IRC Login: USER and NICK
    irc.send(f"NICK {nickname}\r\n".encode())
    irc.send(f"USER {nickname} 0 * :{realname}\r\n".encode())

    # Join the channel after login
    time.sleep(5)  # Wait for server to process login
    irc.send(f"JOIN {channel}\r\n".encode())

    # Simple loop to respond to pings and print messages
    while True:
        response = irc.recv(2048).decode("utf-8", errors="ignore").strip()
        print(response)

        if response.startswith("PING"):
            # Respond to server PINGs to stay connected
            pong_reply = response.replace("PING", "PONG")
            irc.send(f"{pong_reply}\r\n".encode())

        # Optionally, respond to a chat command like "!hello"
        if "PRIVMSG" in response and "!hello" in response:
            sender = response.split("!")[0][1:]
            irc.send(f"PRIVMSG {channel} :Hello, {sender}!\r\n".encode())

main()