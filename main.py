import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt = sys.argv
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

if len(prompt) == 1:
    print("Error")
    sys.exit(1)
else:
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(
        f"Response: {response.text}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}"
    )
