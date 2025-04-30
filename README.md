# Chat_Bot_Software

Create a Chat Bot that connects to IRC Server to talk in a group chat of IRC clients. 

## Table of Contents
<details>
  <summary>Click Me!</summary>

- [Tools and Technologies](#tools-and-technologies)
- [Installation](#installation)
- [Usage](#usage)

</details>

---

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: openai
- **IRC Client**: [mIRC](https://www.mirc.com/)
- **IRC Server**: [UnrealIRCd](https://www.unrealircd.org/download/6.0) 

---

## Installation
1. Create a new directory or folder.
2. Install the mIRC Client.
3. Install the UrealIRCd.
4. Use Github Desktop or git clone to pull the repository to the new directory or folder.
```
git clone https://github.com/BrianDang03/Chat_Bot_Software.git
```
3. Use can use the terminal to change to the Chat_Bot_Software directory. 
```
cd Chat_Bot_Software
```  
4. Use and activate venv or local machine to pip install dependencies.
```
pip install -r requirements.txt
```
---

## Usage

1. After successfully installing IRC client, IRC server, and dependencies, execute the UnrealIRCd.

2. Go to the terminal and type ipconfig and look for the IPv4 Address. This will be the IP address you will use to connect the mIRC client and Chat Bot to the UnrealIRCd server. 

3.  Add your own apikey.txt to the directory, Run the main.py file.
```
python main.py
```

4. Run the UnrealIRCd server, and add the unrealircd.conf file.

5. Run the mIRC Client, add a server to connect to with the same IP and Port Number. Then Connect.

6. Type in the IP Address, a Port number of 6667, and a channel to join.

7. On the mIRC Client join the same channel as the Chat Bot and type something to have a conversation.     

---

