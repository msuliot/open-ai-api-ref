import openai
import _open_api_key
openai.api_key = _open_api_key.get_api_key()

#####################################################

#  ##### Get model list
modelList = openai.Model.list()
print(modelList)