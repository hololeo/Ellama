
# An alarm clock with Ell. 
# work in progress! 

import os
from datetime import datetime
import time
import ell
from openai import OpenAI

MODEL = "llama3.1:8b"

client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

ell.config.verbose = True
ell.config.register_model(MODEL, client)

@ell.tool()
def say_it(text: str):
    print (f"here is your joke:{text}")
    os.system(f"say {text}")
    return "Done"

@ell.tool()
def play_mp3(file_path: str):
    print (f">> playing:{file_path}")
    os.system(f"afplay {file_path}")
    return "Done"

# Function to get just the current time
from datetime import datetime
def get_time_only():
    now = datetime.now()
    # Format: It's now 2:05 PM
    formatted_time = now.strftime("It's now %I:%M:%S %p")
    return formatted_time

@ell.simple(model=MODEL, client=client)
def ell_alarm(alarm_time:str, alarm_action):
    """You are Ell_alarm, an alarm clock. You keep track of user alarms and trigger actions. You are given the current time. When the user alarm time equals or is greater than the current time, you do what the user action requested. Here is example of how user can set an alarm. Example: Ell_alarm: 7:25 remind me to drink water. Response:Its time to drink water mate!"""
    s = get_time_only() + "\n"
    s += f"Ell_alarm: {alarm_time} {alarm_action}"
    return s    

if __name__ == "__main__":
    while True:
        callback = ell_alarm ("08:11:50 AM","finish coding Ell_adventure #8!")
        # for testing every 10 seconds.
        time.sleep(10)
        # more useful to trigger every minute
        #time.sleep(60)
        print (callback)









