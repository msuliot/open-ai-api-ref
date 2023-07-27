import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

#####################################################

#  ##### Get model list
modelList = openai.Model.list()
print(modelList)