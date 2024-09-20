import argparse
import ell
from openai import OpenAI
from PIL import Image

MODEL = "moondream:latest"
client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

ell.config.verbose = True
ell.config.register_model(MODEL, client)

@ell.simple(model=MODEL, client=client)
def make_caption(image_path:str):
    image = Image.open(image_path)
    return [
        ell.system("You caption images."),
        ell.user(["Describe this image",image])
    ]

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate a caption for an image using ELL.")
    parser.add_argument('image_path', type=str, help='Path to the image to be captioned')

    # Parse the arguments
    args = parser.parse_args()

    # Pass the image path from the command line
    result = make_caption(args.image_path)

    print (result)








