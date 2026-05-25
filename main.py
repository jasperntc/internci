import os
from dotenv import load_dotenv
from google import genai
import argparse

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No gemini api key is found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the chatbot")
    args = parser.parse_args()

    model = "gemini-2.5-flash"
    prompt = args.user_prompt

    response = client.models.generate_content(model=model, contents=prompt)

    if response.usage_metadata is None:
        raise RuntimeError("No usage metadata is found in the response")

    print("User prompt: ", prompt)
    print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
