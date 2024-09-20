import argparse
import ell
from openai import OpenAI

MODEL = "llama3.1:8b"

client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

ell.init(store="./logdir")
ell.config.verbose = True
ell.config.register_model(MODEL, client)


@ell.simple(model=MODEL,client=client)
def diffusion_prompt (prompt:str):
    """You are an Advanced AI-assisted prompt engineer specialized in generating high-quality prompts for Stable Diffusion, a state-of-the-art text-to-image generation model. Your task is to create detailed, creative, and contextually relevant prompts that will help users generate desired images effectively. For instance: - A bipedal robotic server, devoid of discernible human features, efficiently sorts and categorizes digital data on its sleek, compact desk. Above the desk, vibrant red letters spell out "ELL-Diffusion" in glowing script, set against a backdrop of red LED strip lighting that casts no shadows. The atmosphere is one of precise orderliness and calculated precision. Style: Cyberpunk, Industrial, Minimalist. Keywords: bipedal robot, digital data sorting, ELL Diffusion, compact desk, red letters. Strive for conciseness, precision, and relevance in all prompts. Stick to the user prompt.
    
    Only respond with the prompt. Do not include preamble or follow up questions"""
    return f"Respond to: {prompt}"


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate a stable diffusion prompt using ELL.")
    parser.add_argument('--prompt', type=str, help='What image do you want?', default="A male bipedal robotic server, devoid of discernible human features, efficiently sorts and categorizes digital data on its sleek, compact desk. Above the desk, vibrant red letters spell out 'ELL-Diffusion' in glowing script, set against a backdrop of red LED strip lighting that casts no shadows. The atmosphere is one of precise orderliness and calculated precision. Style: Cyberpunk, Industrial, Minimalist. Keywords: bipedal robot, digital data sorting, ELL Diffusion, compact desk, red letters.")


    # Parse the arguments
    args = parser.parse_args()

    # Pass the image path from the command line
    result = diffusion_prompt(args.prompt)

    print (result)



