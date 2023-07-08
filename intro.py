import openai
import webbrowser
openai.api_key = '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'

def open_image(url):
    webbrowser.open(url)

#####################################################

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
#     {"role": "system", "content": "You are a helpful assistant and expert in World War I history."},
#     {"role": "user", "content": "Hello! My name is Jimmy Jo Bob."},
#     {"role": "assistant", "content": "Hello Jimmy Jo Bob! It's nice to meet you. How can I assist you today?"},
#     {"role": "user", "content": "What caused World War I?"},
#     {"role": "assistant", "content": "World War I was caused by a combination of factors, including nationalism, imperialism, militarism, and the assassination of Archduke Franz Ferdinand of Austria."},
#     {"role": "user", "content": "who won?"},
#   ]
# )
# # print(completion) # prints the whole response in JSON format
# print(completion.choices[0].message["content"]) # prints the first response from the "assistant role"

#####################################################



# 3 ##### Create a simple image # required parameters: prompt
# createImage = openai.Image.create(
#             prompt="my dog driving a sports car",
#             n=1, # The number of images to generate
#             size="1024x1024",
#             user="MichaelAI", # name of the user
#             response_format="url" # url is default but can also be 'b64_json'
#         )
# image_url_3 = createImage['data'][0]['url']
# open_image(image_url_3)

#####################################################

# 4 ##### Edit a image by adding something to the transparency layer
# editImage = openai.Image.create_edit(
#   image=open("images/transparency.png", "rb"),
#   prompt="add some mountains in the background, and a nebula in the sky",
#   n=1, # The number of images to generate
#   size="1024x1024",
#   user="MichaelAI", # name of the user
# )
# image_url_4 = editImage['data'][0]['url']
# open_image(image_url_4)

#####################################################

# 5 ##### Create image variation
variation = openai.Image.create_variation(
  image=open("images/michael.png", "rb"),
  n=1,
  size="1024x1024",
  user="MichaelAI", # name of the user
)
image_url_5 = variation['data'][0]['url']
open_image(image_url_5)

#####################################################

# 6 ##### Speech to text # currently limited to 25 MB
# audio_file= open("audio/iphone.m4a", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
# print(transcript)

#####################################################

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Create an analogy for this phrase:\n\nQuestions are arrows in that:",
#   temperature=0.5,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )




#####################################################
#####################################################
#####################################################
#####################################################
#####################################################

# 7 ##### Creates a vector representing the input. # required parameters: model, input
# note:  this will generate an array of around 1536 floats numbers 0.0049300906248390675, -0.006244358140975237,
# embedding = openai.Embedding.create(
#   model="text-embedding-ada-002",
#   input="I really enjoy walking my dog in the park.",
#   user="MichaelAI", # name of the user
# )
# print(embedding)

#####################################################

# 8 ##### Files
# files = openai.File.list()
# print(files)
#### FineTune
# ft = openai.FineTune.list()
# print(ft)

#####################################################

# 9 ##### Upload a file and fine tune # required parameters: file, purpose # Your data must be a JSONL document
# upload = openai.File.create(
#   file=open("jsonl/testing.jsonl", "rb"),
#   purpose='fine-tune',
# )
# print(upload)

# id_value = upload["id"]

# fineTune = openai.FineTune.create(training_file=id_value)
# print(fineTune)

#####################################################

# 10 ##### Delete a file # required parameters: id
# print(openai.File.delete("file-pXmhwevkvift4nYU3YIxMRNF"))
# print(openai.File.delete("file-GM7OWHi35dZAH3yQ5QlxvCJP"))
# print(fDel)
# files = openai.File.list()
# print(files)

# print(openai.FineTune.cancel(id="ft-p0Ke7O3SifsRTm4TJPPURmbi"))
# print(openai.Model.delete("curie"))




#####################################################

# 11 ##### Retrieve a file info # required parameters: id
# file = openai.File.retrieve("file-OxblrdAlekTQ9i0QzptVyMqm")
# print(file)

#####################################################

# 12 ##### Download a file # required parameters: id
# content = openai.File.download("file-OxblrdAlekTQ9i0QzptVyMqm")
# print(content)

#####################################################

# 13 ##### 
# import json
# jData = '''{
#   "object": "file",
#   "id": "file-pXmhwevkvift4nYU3YIxMRNF",
#   "purpose": "fine-tune",
#   "filename": "file",
#   "bytes": 151,
#   "created_at": 1688780901,
#   "status": "uploaded",
#   "status_details": null
# }
# '''

# data = json.loads(jData)
# id_value = data["id"]
# print(id_value)




    