import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Create image variation
variation = openai.Image.create_variation(
    image=open("images/michael.png", "rb"),
    n=2, # The number of images to generate
    size="1024x1024",
    user="MichaelAI", # name of the user
    response_format="url" # url is default but can also be 'b64_json'
)

for item in variation["data"]:
    open_image(item["url"])

# image_url_5 = variation['data'][0]['url']
# open_image(image_url_5)



