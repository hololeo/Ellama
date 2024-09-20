import ell
from openai import OpenAI
import os

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

@ell.complex(model=MODEL, client=client, tools=[say_it])
def make_joke(topic:str):
    """You are a funny but corny comedy writer. Return a joke about the users topic. Review your joke. Remove emojis. Only return the joke. Do not provide commentary about the joke"""
    return f"come up with a joke about {topic}. In your response do not include emojis. Do not include any commentary on the joke."    

if __name__ == "__main__":
    user_prompt = "AI"
    callback = make_joke (user_prompt)
    print (callback)
    callback.tool_calls[0]()








