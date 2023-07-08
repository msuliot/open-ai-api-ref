import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()

#####################################################

#  ##### Simple completion # required parameters: model, messages[], role
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
# print(completion) # prints the whole response in JSON format
print(completion.choices[0].message["content"]) # prints the first response from the "assistant role"