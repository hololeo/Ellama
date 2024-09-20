import argparse
import ell
from openai import OpenAI
from PIL import Image

MODEL = "llama3.1:8b"
#MODEL = "qwen2.5:0.5b"
client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

ell.config.verbose = True
ell.config.register_model(MODEL, client)

def make_description_html(ai_text: str, script_name:str, script_link:str):
    s = f"""<table>
  <tr>
    <td  width="300"><img src="https://user-images.githubusercontent.com/11970940/190875540-d45afb9a-9d09-44b0-93c4-8159b28ea6df.png" alt="{script_name} Icon"></td>
    <td align="left" valign="top"><strong><a href="{script_link}">{script_name}</a>
    </strong>{ai_text}</td>
  </tr>
</table>
"""
    return s


@ell.simple(model=MODEL, client=client)
def make_project_description(script_name:str, script_description:str):
    return [
        ell.system("Write a brief plain text description for the user_script_name Name and Description. It starts with the name of the script and a link to the github repo using https://github.com/hololeo/Ellama/blob/main/ + script name using pattern in Example. The description should include what the script does, the technologies or libraries it uses. The audience is an AI developer. Make the description detailed but concise. No more than 3 sentences. Example: ```ell-captioner.py https://github.com/hololeo/Ellama/blob/main/ell-captioner.py is a Python script designed for fast image captioning. It generates descriptive captions from input images. The script utilizes Ollama to run the Moondream language model locally and leverages the Ell library to structure system and user prompts effectively. You can pass the image as an argument via the command line, and the script will provide an accurate and contextually aware caption for the image.``` Ignore the Name of the script in your understanding. Do not provide markdown. Do not provide commentary.  Do not embelish. Do not include an introduction. Do not include a conclusion"),
        ell.user(f"Name:{script_name}\n Description:{script_description}")
    ]

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate a stable diffusion prompt using ELL.")
    parser.add_argument('--script_name', type=str, help='Name of script', default="Ell-difussion.py")
    parser.add_argument('--script_thumbnail', type=str, help='Image thumbnail url', default="https://user-images.githubusercontent.com/11970940/190875540-d45afb9a-9d09-44b0-93c4-8159b28ea6df.png")
    parser.add_argument('--script_description', type=str, help='Description of script', default="This script shows how to take a user prompt for an image and create a better prompt for stable diffusion. It uses Ell to talk to a local LLama3.1 model and create a prompt optomized for stable diffusion.")

    # Parse the arguments
    args = parser.parse_args()
    script_name = args.script_name
    script_link = f"https://github.com/hololeo/Ellama/blob/main/{script_name}.py"

    # Pass the image path from the command line
    ai_text = make_project_description(args.script_name,args.script_description)
    new_html = make_description_html (ai_text, script_name, script_link)
    print (ai_text)
    print (new_html)