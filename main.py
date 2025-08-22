import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt = sys.argv
system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

if len(prompt) == 1:
    print("Error: No prompt/arguments given.")
    sys.exit(1)
elif len(prompt) == 2:
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt[1])]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    print(f"Response: {response.text}")

elif len(prompt) == 3:
    if prompt[2] == "--verbose":
        messages = [
            types.Content(role="user", parts=[types.Part(text=prompt[1])]),
        ]

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )

        print(
            f"User prompt: {prompt[1]}\n\nResponse: {response.text}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}"
        )
    else:
        print("Error: Invalid argument given with prompt.")
