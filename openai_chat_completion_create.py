import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

#####################################################

#  ##### Simple completion # required parameters: model, messages[], role
# print(completion) # prints the whole response in JSON format
try:
    completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # from the model list
  temperature=0.3, # 0.0 - 2.0 Low number=highly focused, higher number = randomness and embellishing
  n=1, # number of responses to return
  user="MichaelAI", # name of the user
  messages=[
    {"role": "system", "content": "You are a helpful assistant and expert in World War I history."},
    {"role": "user", "content": "Hello! My name is Jimmy Jo Bob."},
    {"role": "assistant", "content": "Hello Jimmy Jo Bob! It's nice to meet you. How can I assist you today?"},
    {"role": "user", "content": "What caused World War I?"},
    {"role": "assistant", "content": "World War I was caused by a combination of factors, including nationalism, imperialism, militarism, and the assassination of Archduke Franz Ferdinand of Austria."},
    {"role": "user", "content": "who won?"},
    {"role": "assistant", "content": "The Allied Powers, which included countries such as France, Britain, Russia, and later the United States, emerged as the victors of World War I. The Central Powers, consisting of Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria, were defeated. The war officially ended with the signing of the Treaty of Versailles in 1919"},
    {"role": "user", "content": "What was the Treaty of Versailles?"},
  ]
)
except openai.error.APIError as e:
    #Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    pass
except openai.error.APIConnectionError as e:
    #Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")
    pass
except openai.error.RateLimitError as e:
    #Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass
except openai.error.AuthenticationError as e:
    #Handle authentication error (e.g. invalid credentials)
    print(f"OpenAI API request failed due to invalid credentials: {e}")
    pass
except openai.error.InvalidRequestError as e:
    #Handle invalid request error (e.g. required parameter missing)
    print(f"OpenAI API request failed due to invalid parameters: {e}")
    pass
except openai.error.ServiceUnavailableError as e:
    #Handle service unavailable error
    print(f"OpenAI API request failed due to a temporary server error: {e}")
    pass
else:
    # code to execute if no exception was raised
    print(completion.choices[0].message["content"]) # prints the first response from the "assistant role"
