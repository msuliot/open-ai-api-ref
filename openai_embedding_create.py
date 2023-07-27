import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

#####################################################

#  ##### Creates a vector representing the input. # required parameters: model, input
#note:  this will generate an array of around 1536 floats numbers 0.0049300906248390675, -0.006244358140975237,
embedding = openai.Embedding.create(
  model="text-embedding-ada-002",
  input="I really enjoy walking my dog in the park.",
  user="MichaelAI", # name of the user
)
print(embedding)