import openai
import _open_api_key
openai.api_key = _open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Edit a image by adding something to the transparency layer
editImage = openai.Image.create_edit(
  image=open("images/transparency.png", "rb"),
  prompt="add some mountains in the background, and a nebula in the sky",
  n=1, # The number of images to generate
  size="1024x1024",
  user="MichaelAI", # name of the user
)
image_url_4 = editImage['data'][0]['url']
open_image(image_url_4)

