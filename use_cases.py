import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()
import Util

#####################################################

transcript = Util.audio_to_text("audio/happy.m4a") # convert audio to text
response = Util.get_completion(Util.create_prompt(transcript)) # create prompt with text and instructions on how to respond
print(response)

transcript = Util.audio_to_text("audio/mad.m4a")
response = Util.get_completion(Util.create_prompt(transcript))
print(response)