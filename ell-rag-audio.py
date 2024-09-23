import ell
from openai import OpenAI
import argparse

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
def ask_audio (transcript:str, prompt:str):
    """Your name is Ell_rag_audio. You are an expert at responding to prompts that contain audio transripts, audio books, youtube videos, songs, anything and everything else with audio. It comes to you by text so you have expert ability in interpreting and locating in the text. If timecodes are available, provide the timecode and complete line to support your response."""
    s = f"Context:\n -------- \n {transcript} -------- \n"
    s += f"User: {prompt}\n"
    return s    

if __name__ == "__main__":
    user_prompt = "what is this about?"
    input_file = "transcript.txt"
    transcript_txt = read_and_normalize_file(input_file)
    response = ask_audio (transcript_txt, user_prompt)
    print (response)