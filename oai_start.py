from langchain.llms import LlamaCpp
from langchain import PromptTemplate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# A function that returns persona to be set for the chat. Use the type provided as input to determine the personality prompt that should be passed to OpenAI
def get_personality_prompt(type):
    # use type argument to generate different types of personalities
    if type == 1:
        # return a personality prompt for a friendly chat
        return "I am a very friendly person. I love to talk about movies and books. {text}"
    elif type == 2:
        # return a personality prompt for a professional chat
        return "I am a very professional person. I love to talk about my work and my hobbies. {text}"
    else:
        # return a personality prompt for a neutral chat
        return "I am a very neutral person. I love to talk about my work and my hobbies. {text}"
    
# A function that returns the response from OpenAI
def get_response(prompt, type=1):
    # Using the openai library, call the completion endpoint and pass the prompt as input
    template = get_personality_prompt(type) + prompt

    prompt_template = PromptTemplate(template=template, input_variables=["text"])
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = LlamaCpp(
        model_path="/home/jerrykurian/Public/code/llama/llama.cpp/models/llama-2-7b-chat.ggmlv3.q8_0.bin",
        temperature=0.75,
        max_tokens=2000,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True,
    )
    prompt_template = prompt
    llm(prompt_template)

var = input("Please enter prompt: ")
get_response(var, 1)