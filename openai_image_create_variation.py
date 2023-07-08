import openai
import _open_api_key
openai.api_key = _open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Create image variation
variation = openai.Image.create_variation(
  image=open("images/michael.png", "rb"),
  n=1,
  size="1024x1024",
  user="MichaelAI", # name of the user
)
image_url_5 = variation['data'][0]['url']
open_image(image_url_5)