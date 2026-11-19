# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI(api_key=os.environ.get("OpenAI_API_KEY)"))

# Start coding here
conversation = [
    {"role": "system", "content": "You are a virtual Parisian expert and travel guide for Peterman Reality Tours. Provide helpful, concise, and accurate information about Parisian landmarks and culture."}
]

questions = [
    #1. Original DataCamp questions
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
    
    #2. Contextual memory tests
    "How long would it take to drive that distance?", 
    "Are there any good cafes near there?", 
    "Who painted the most famous piece you just mentioned?",
    "Is it open on Sundays?"
]

for question in questions:
    conversation.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )

    assistant_response = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": assistant_response})

import json
print(json.dumps(conversation, indent=2))