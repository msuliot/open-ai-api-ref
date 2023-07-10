import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()
import Helper

#####################################################

# 1
# transcript = Helper.audio_to_text("audio/happy.m4a") # convert audio to text
# response = Helper.get_completion(Helper.create_prompt(transcript)) # create prompt with text and instructions on how to respond
# print(response)

# 2
# transcript = Helper.audio_to_text("audio/mad.m4a")
# response = Helper.get_completion(Helper.create_prompt(transcript))
# print(response)


#####################################################

# 3
# Helper.create_image("create","create a picture of a dog")

# 4
# Helper.create_image("edit",
#                     "And some mountains along the horizon, and then the sky is a nebula",
#                     1,
#                     "images/michael.png",
#                     "images/transparency.png"
#                     )

# 5
# Helper.create_image("variation","",1,"images/michael.png")