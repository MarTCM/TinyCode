import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if (api_key == None):
    raise RuntimeError("GEMINI_API_KEY environment variable not set")

client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="AI Code Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=args.user_prompt)])]

    generate_content(client, messages)

def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    print("User prompt: " + args.user_prompt)

    if (response.usage_metadata != None):
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
        print("Response:")
        print(response.text)
    else:
        raise RuntimeError("API call failed")

if __name__ == "__main__":
    main()
