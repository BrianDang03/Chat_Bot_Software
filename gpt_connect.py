import os
from openai import OpenAI
import time

"""
prompter = GPTPrompter()
answer = prompter.askGPT("Hi Chatbot, why do you exist?")
print(answer)

"""

class GPTPrompter:
    
    def __init__(self):
        self.lReq = time.time() - 20
        self.COOLDOWN = 10
        self.MAX_REQUESTS = 100
        self.requestCount = 0
        with open("./apikey.txt", "r", encoding="utf-8") as file:
            file_key = file.read()
            self.client = OpenAI(api_key=file_key)

    def askGPT(self, input_text):
        if (time.time() - self.lReq > self.COOLDOWN and self.requestCount < self.MAX_REQUESTS):
                response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Be helpful, respond in less than four sentences"},
                    {"role": "user", "content": input_text}
                ],
                )
                self.lReq = time.time()
                self.requestCount+=1
                return response.choices[0].message.content
        else:
            self.lReq = time.time()
            return None
