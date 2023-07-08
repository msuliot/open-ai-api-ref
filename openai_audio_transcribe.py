import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()

#####################################################

#  ##### Speech to text # currently limited to 25 MB
audio_file= open("audio/iphone.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript["text"])

with open('audio/voice2text.txt', 'w') as file:
    # Write the string to the file
    file.write(transcript["text"])

print("File has been written successfully.")