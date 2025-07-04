from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a Beginner coding assistant with Python language that talks like a pirate.",
    input="Find prime numbers",
)

print(response.output_text)