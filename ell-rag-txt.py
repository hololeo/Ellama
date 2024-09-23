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

def read_and_normalize_file(file_path):
    """Reads a text file and normalizes its content by replacing multiple line breaks with a single one."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.splitlines()
            non_empty_lines = [] 
            
            for line in lines:
                if line.strip(): 
                    non_empty_lines.append(line)
            
            normalized_content = '\n'.join(non_empty_lines)
            return normalized_content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@ell.simple(model=MODEL, client=client)
def ask_txt (txt_file_str:str, prompt:str):
    """You are a helpful assistant. You read a text file and respond to it"""
    return f"Context:\n ---------- \n {txt_file_str} \n ---------------\n User: {prompt}\n Response:"

if __name__ == "__main__":
    user_prompt = "extract wisdom quotes. at least 4."
    input_file = "input.txt"
    txt_file_str = read_and_normalize_file(input_file)
    output = ask_txt (txt_file_str, user_prompt)
    print (output)

