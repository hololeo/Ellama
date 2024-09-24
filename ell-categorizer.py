import ell
from openai import OpenAI
import argparse
from typing import List, Dict
import json

MODEL = "llama3.1:8b"
MODEL = "gemma2:2b"

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama",
)

ell.config.verbose = True
ell.config.register_model(MODEL, client)

def save_response_to_file(response, filename='categories.json'):
    with open(filename, 'w') as file:
        file.write(response)

# prompt hat tip: @MrDragonFox
@ell.simple(model=MODEL, client=client)
def classify_prompts (prompt:str):
    """Your name is Ell_categorizer. You are a helpful assistant that categorizes various types of prompts or ideas."""
    s = f"""
Analyze and categorize each of the following prompts or ideas. 
Create appropriate category labels based on the content and themes you observe.
Provide the result as a JSON array where each element is an object with 'id' (number), 'prompt', 'categories' (an array of category labels), and 'explanation' keys.

Be consistent with category labels across similar prompts.
Always include the 'explanation' for your categorization.
Only provide the JSON array in your response. 
Do not use returns or spaces in your json.
Do not return any markdown code. only json.
Carefully re-read these instructions again before proceeding.

Example:

Input: 30. Craft a persuasive [type of blog post] that showcases the unique features and benefits of your [product/service], specifically tailored to the needs and preferences of your [ideal customer persona], and provide a clear and actionable call-to-action to drive conversion.

Output:{{"🤖id": 30 ,"prompt": "Craft a persuasive [type of blog post] that showcases the unique features and benefits of your product/service, specifically tailored to the needs and preferences of your ideal customer persona.",
"categories": 
['Benefit Driven Content', 'Marketing Strategy','Niche Targeting'],
"explanation": " This involves creating compelling content focused on the specific aspects of a product or service that appeal directly to desired customers."}},

Input: 24. Compose an email that emphasizes the convenience and ease of use of your [product/service] and how it can simplify the lives of your [ideal customer persona]. Use persuasive language to address any concerns or objections and encourage them to take the desired action.

Output:{{"🤖id": 24 ,"prompt": "Compose an email that emphasizes the convenience and ease of use of your product/service and how it can simplify the lives of your ideal customer persona. Use persuasive language to address any concerns or objections and encourage them to take the desired action.",
"categories":
['Marketing Strategy', 'Content Focus on Ease of Use']}},

Now do it to these prompts

Prompts: {prompt}
"""
    return s

# make this as long as your context window allows, or batch it in bit by bit
prompts = """
23. Write an email that connects with the personal values and desires of your [ideal customer persona] and positions your [product/service] as the key to achieving their goals. Use persuasive language and a strong call-to-action to encourage them to take the desired action.
24. Compose an email that emphasizes the convenience and ease of use of your [product/service] and how it can simplify the lives of your [ideal customer persona]. Use persuasive language to address any concerns or objections and encourage them to take the desired action.
25. Craft an email that showcases the expertise and authority of your brand by offering valuable insights and tips related to your [product/service]. Use persuasive language and a strong call-to-action to encourage them to take the desired action and engage with your brand further.
"""

if __name__ == "__main__":
    json_response = classify_prompts (prompt=prompts)
    print (json_response)
    save_response_to_file(json_response)
