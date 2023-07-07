import openai
openai.api_key = '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'

# 1 ##### Get model list
# modelList = openai.Model.list()
# print(modelList)

#####################################################

# 2 ##### Simple completion # required parameters: model, messages[], role
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo", # from the model list
#   temperature=0.3, # 0.0 - 2.0 Low number=highly focused, higher number = randomness and embellishing
#   n=1, # number of responses to return
#   user="MichaelAI", # name of the user
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello! My name is Michael AI."},
#   ]
# )
# # print(completion) # prints the whole response in JSON format
# print(completion.choices[0].message) # prints the first response from the "assistant role"

#####################################################

# 3 ##### Create a simple image # required parameters: prompt
# createImage = openai.Image.create(
#             prompt="A painting of a forest",
#             n=1, # The number of images to generate
#             size="1024x1024",
#             user="MichaelAI", # name of the user
#             response_format="url" # url is default but can also be 'b64_json'
#         )
# image_url_3 = createImage['data'][0]['url']
# print(image_url_3) # prints the whole response in JSON format   

#####################################################

# 4 ##### Edit a image by adding something to the transparency layer
editImage = openai.Image.create_edit(
  image=open("images/transparency.png", "rb"),
  prompt="Had some mountains in the background",
  n=1, # The number of images to generate
  size="1024x1024",
  user="MichaelAI", # name of the user
)
image_url_4 = editImage['data'][0]['url']
print(image_url_4)

#####################################################

# 5 ##### Create image variation
# variation = openai.Image.create_variation(
#   image=open("images/michael.png", "rb"),
#   n=1,
#   size="1024x1024",
#   user="MichaelAI", # name of the user
# )
# image_url_5 = variation['data'][0]['url']
# print(image_url_5)

#####################################################

# 6 ##### Creates a vector representing the input. # required parameters: model, input
# note:  this will generate an array of around 1536 floats numbers 0.0049300906248390675, -0.006244358140975237,
# embedding = openai.Embedding.create(
#   model="text-embedding-ada-002",
#   input="I really enjoy walking my dog in the park.",
#   user="MichaelAI", # name of the user
# )
# print(embedding)

#####################################################

# # 7 ##### Speech to text # currently limited to 25 MB
# audio_file= open("audio/iphone.m4a", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
# print(transcript)

#####################################################