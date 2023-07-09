import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Create a simple image # required parameters: prompt
createImage = openai.Image.create(
            prompt="abstract art of earth from space",
            n=1, # The number of images to generate
            size="1024x1024",
            response_format="url" # url is default but can also be 'b64_json'
        )

for item in createImage["data"]:
    open_image(item["url"])

# image_url_3 = createImage['data'][0]['url']
# open_image(image_url_3)
