# utils.py
import openai
from openai import OpenAI

# Set your OpenAI API key
openai.api_key = "XXX"

def getPrompt(input):
    messages = [
        {"role": "user", "content": f"{input}"}
    ]

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai.api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages # type: ignore
    )
    reply = completion.choices[0].message.content
    return reply
