import ell
from openai import OpenAI

MODEL = "gemma2:2b"
#MODEL = "tinyllama:latest"

client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

#ell.init(store="./logdir")
ell.config.verbose = True
ell.config.register_model(MODEL, client)


@ell.simple(model=MODEL,client=client)
def summarize_text(prompt:str):
    """Summarize the given text in bullet points. Use simple English. Be concise. Summaries can not exceed 2 sentences. Format each summary as a single bullet list with each sentence in 
the same list. Use * for each bullet point. Avoid any introduction, preamble, or conclusion. Do not use markdown formatting"""
    return f"Respond to: {prompt}"

if __name__ == "__main__":
    user_prompt = """Climate Change:
Climate change refers to long-term shifts in temperatures and weather patterns, primarily due to human activities. The burning of fossil 
fuels releases greenhouse gases, trapping heat in the atmosphere. This results in melting glaciers, rising sea levels, and more extreme 
weather events."""
    output = summarize_text (user_prompt)
    print (output)





