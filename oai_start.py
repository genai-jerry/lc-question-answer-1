import os
import openai

# A function that returns persona to be set for the chat. Use the type provided as input to determine the personality prompt that should be passed to OpenAI
def get_personality_prompt(type):
    # use type argument to generate different types of personalities
    if type == 1:
        # return a personality prompt for a friendly chat
        return "I am a very friendly person. I love to talk about movies and books."
    elif type == 2:
        # return a personality prompt for a professional chat
        return "I am a very professional person. I love to talk about my work and my hobbies."
    else:
        # return a personality prompt for a neutral chat
        return "I am a very neutral person. I love to talk about my work and my hobbies."
    
# A function that returns the response from OpenAI
def get_response(prompt, type=1):
    # Using the openai library, call the completion endpoint and pass the prompt as input
    prompt = get_personality_prompt(type) + prompt
    print(prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return response

# a function to extract the choices from the OpenAI completion response
def get_choices(response):
    # get the choices from the response
    choices = response['choices']
    # return the text of the first choice
    return choices[0]['text']

# read the API key from the environment variable
var = input("Please enter your openAI key: ")
openai.api_key = var
print(openai.api_key)

var = input("Please enter something: ")
response = get_response(var, 1)
print(get_choices(response))
print(response)