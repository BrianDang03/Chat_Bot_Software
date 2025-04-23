import os
from openai import OpenAI
import time


# Returns string response or NONE
# Make sure to pass the last time
def askGPT(input, lReq):
    COOLDOWN = 10
    if (time.time() - lReq > COOLDOWN):
        with open("./apikey.txt", "r", encoding="utf-8") as file:
            client = OpenAI(api_key=file.read())

            response = client.responses.create(
            model="gpt-4o-mini",
            instructions="Be helpful, respond in less than four sentences",
            input=input,
            )
            return response.output_text
    else:
        lReq = time.time()
        return None
