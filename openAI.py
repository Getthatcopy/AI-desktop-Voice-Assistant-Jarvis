from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="API_KEY")

# Create a completion request
completion = client.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

# Print the generated poem
print(completion.choices[0].message["content"])
