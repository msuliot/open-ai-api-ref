import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Edit a image by adding something to the transparency layer
editImage = openai.Image.create_edit(
  image=open("images/michael.png", "rb"),
  mask=open("images/transparency.png", "rb"),
  prompt="And some mountains along the horizon, and then the sky is a nebula",
  n=2, # The number of images to generate
  size="1024x1024",
)

for item in editImage["data"]:
    open_image(item["url"])

# image_url_4 = editImage['data'][0]['url']
# open_image(image_url_4)